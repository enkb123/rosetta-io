from collections.abc import Callable
import os.path
import subprocess
import sys
from abc import ABC
from dataclasses import dataclass
from typing import IO

import docker
import pytest

from locking import EarlyBirdLock, early_bird_lock

type EarlyBirdLocker = Callable[[list[str]], EarlyBirdLock]


@pytest.fixture
def once_per_test_suite_run(
    tmp_path_factory: pytest.TempPathFactory, testrun_uid: str, worker_id: str
) -> EarlyBirdLocker:
    """Fixture that provides a context manager for a lock that is only allowed
    to be acquired once per test suite run"""

    return lambda lock_keys: early_bird_lock(
        tmp_path_factory.getbasetemp().parent,
        testrun_uid,
        *lock_keys,
        worker_id=worker_id,
    )


class Language(ABC):
    """Abstract base class representing a the settings for a language."""

    name: str
    """The name of the language, e.g. "python" or "ruby"."""

    interpreter: str
    """The interpreter to use to run the script,
    e.g. if `interpreter` is "python" then `script.py` will be run via `python script.py`
    """

    script_ext: str
    """The file extension of the script, e.g. ".py" or ".R" or ".java"."""

    def script_file_name(self, script_name):
        """Given a name of a script, return the file name of the script to run.

        e.g. for Python, if `script_name` is "null_char", then this returns "null_char.py"
        Subclasses can override this, e.g. for Java, we'd want this to return "NullChar.java"
        """
        return f"{script_name}{self.script_ext}"

    def command(self, test_name):
        """Return the shell command that executes the script

        e.g. for Python, this returns "python null_char.py"
        and for R, this returns "Rscript null_char.R"
        """
        return f"{self.interpreter} {self.script_file_name(test_name)}"

    @property
    def directory(self):
        """The directory in which this language's scripts are stored

        e.g. for Python, this is 'python'
        """
        return self.name

    def script_local_file(self, script_name):
        """Given a name of a script, return the local file path of the script to run.

        E.g. for Python, if `script_name` is "null_char", then this returns "python/null_char.py"
        """
        return os.path.join(self.directory, self.script_file_name(script_name))


@dataclass
class ScriptRunner(ABC):
    """Class that handles script execution"""

    language: Language
    # container: docker.models.containers.Container = None
    cwd: str | None = None
    output: str = None
    stdin: IO[str] = None
    stdout: IO[str] = None
    stderr: IO[str] = None

    def build_command(self, script_name, rest_of_script):
        """
        Constructs the shell command to execute the script with the given arguments.

        Args:
            script_name (str): The name of the script to execute.
            rest_of_script (str): Additional arguments or options to pass to the script.

        Returns:
            list: The constructed shell command as a list of strings.
        """
        return [
            "/bin/sh",
            "-c",
            f"{self.language.command(script_name)} {rest_of_script}",
        ]

    @property
    def subprocess_params(self):
        """
        Constructs and returns the parameters for subprocess calls.

        Returns:
            dict: Dictionary of parameters to be used in subprocess calls.
        """
        return dict(
            cwd=self.cwd,
            text=True,  # treat standard streams as text, not bytes
            bufsize=1,  # set 1 for line buffering, so buffer is flushed when encountering `\n`
        )

    def _run(self, command):
        completed_process = subprocess.run(
            command,
            capture_output=True,  # wait for script to complete
            check=True,  # explicitly define the value for 'check'
            **self.subprocess_params,
        )
        print(completed_process.stderr, file=sys.stderr)
        return completed_process

    def _run_interactive(self, command):
        running_process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            **self.subprocess_params,
        )
        self.stdin = running_process.stdin
        return running_process

    def run(self, script_name, rest_of_script="", interactive=False):
        """
        Execute the given script.

        Parameters:
            script_name (str): The name of the script to execute. e.g. "null_char"

            rest_of_script (str): Additional parameters or script contents to run.
                e.g. "< hihello.txt"

            interactive (bool): Whether to run the script interactively or wait until it completes.
        """
        if not os.path.isfile(self.language.script_local_file(script_name)):
            pytest.skip(
                f"Script {repr(script_name)} is not implemented"
                f" for language {repr(self.language.name)}"
            )

        command = self.build_command(script_name, rest_of_script)

        print("command:", command)

        if interactive:
            script_process = self._run_interactive(command)
        else:
            script_process = self._run(command)

        self.output = script_process.stdout
        self.stdout = script_process.stdout
        self.stderr = script_process.stderr


class DockerRunner(ScriptRunner):
    """Runner that runs the script in a docker container"""

    image: str

    def __init__(self, language, image):
        super().__init__(language)
        self.image = image

    def build_command(self, *command_args):
        """Build the command to run the script in docker"""
        return [
            "docker",
            "run",
            "-i",
            self.image,
            *super().build_command(*command_args),
        ]


class LocalRunner(ScriptRunner):
    """Runner that runs the script locally by cd'ing into the language directory
    and running the script"""

    @property
    def cwd(self):
        """Use the directory with named after the language"""
        return self.language.name


class DockerBuilder:
    """Builds docker images"""

    def __init__(self, early_bird_locker: EarlyBirdLocker):
        self.docker_client = docker.from_env()
        self.early_bird_locker = early_bird_locker

    def build(self, build_context: str, image_name: str):
        """Builds the docker image, given the build context and image name"""
        _, logs = self.docker_client.images.build(path=build_context, tag=image_name)
        for chunk in logs:
            if stdout_chunk := chunk.get("stream"):
                print(stdout_chunk, end="")

    def docker_image(self, language_name: str) -> str:
        """Fixture that returns the image name to use for running the script under test, but first
        ensures that the image is built if it is not already.

        Uses the `once_per_test_suite_run` fixture to ensure that the image is only
        built once per test suite run, even for multiple workers.
        """

        image_name = f"{language_name}-rosetta"
        build_context = f"./{language_name}/"

        # Only allow the first pytest-xdist worker that gets here to build the
        # image. Otherwise, they will all try to build it and clobber each other.
        with self.early_bird_locker(["build-image", image_name]) as should_build:
            # should_build will be True if this is the the first worker to get here, otherwise False
            if should_build:
                self.build(build_context, image_name)

        return image_name

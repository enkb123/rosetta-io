import os.path
import shlex
import subprocess
import sys
import textwrap
from abc import ABC
from dataclasses import dataclass, field
from pathlib import Path
from re import sub
from typing import IO

import docker
import pytest

from locking import EarlyBirdLocker


def print_command(title: str, command: str) -> None:
    """Prints the given command in a way to make it easier to pick out of pytest output"""
    longest_line_length = max(
        min(max(map(len, command.split("\n"))), 80), len(title) + 2
    )
    print("┌" + "─" * (len(title)) + "┐")
    print(f"│{title}│")
    print("┷" + "━" * (longest_line_length - 1))
    print(command.strip())
    print("━" * (longest_line_length))
    print()


def dedent(text: str) -> str:
    """Dedents the given text"""
    return textwrap.dedent(text).lstrip()


def camel_case(s):
    """Converts a string to camel case"""
    # Use regular expression substitution to replace underscores and hyphens with spaces,
    # then title case the string (capitalize the first letter of each word), and remove spaces
    return sub(r"(_|-)+", " ", s).title().replace(" ", "")


@pytest.fixture
def once_per_test_suite_run(
    tmp_path_factory: pytest.TempPathFactory, testrun_uid: str, worker_id: str
) -> EarlyBirdLocker:
    """Fixture that provides a context manager for a lock that is only allowed
    to be acquired once per test suite run"""

    return EarlyBirdLocker(
        testrun_uid,
        tmp_dir=tmp_path_factory.getbasetemp().parent,
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

    human_name: str
    """The human name of the language e.g. "C#" vs "Csharp"."""

    syntax_highlighting: str
    """Syntax_highlighting for langueage, e.g. "javascript" for deno."""

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
class SetupPair:
    """Prepare and cleanup commands for a script"""
    prepare: str | None
    cleanup: str | None


@dataclass
class ScriptRunner(ABC):
    """Class that handles script execution"""

    language: Language

    files: dict[str, str] = field(default_factory=dict)

    setup_pairs: list[SetupPair] = field(default_factory=list)

    output: str = None
    stdin: IO[str] = None
    stdout: IO[str] = None
    stderr: IO[str] = None

    def setup(self, prepare: str = None, cleanup: str = None):
        """Adds a setup step to the script runner"""
        self.setup_pairs.append(
            SetupPair(
                prepare and dedent(prepare),
                cleanup and dedent(cleanup),
            )
        )

    @property
    def file_setup_pairs(self) -> list[SetupPair]:
        """Returns a list of SetupPairs to create and clean up the files in self.files"""
        return [
            SetupPair(
                f"> {file_name} printf %s {shlex.quote(file_contents)}",
                f"rm {file_name}",
            )
            for file_name, file_contents in self.files.items()
        ]

    @property
    def all_setup_pairs(self) -> list[SetupPair]:
        """Returns a list of all the setup pairs, including the file setup pairs"""
        return self.setup_pairs + self.file_setup_pairs

    @property
    def prepare_commands(self) -> list[str]:
        """Returns a list of the all the prepare commands"""
        return [pair.prepare for pair in self.all_setup_pairs if pair.prepare]

    @property
    def cleanup_commands(self) -> list[str]:
        """Returns a list of the all the cleanup commands"""
        return [pair.cleanup for pair in self.all_setup_pairs if pair.cleanup]

    def add_named_pipe(self, *pipe_names: list[str]):
        """Adds a named pipe to the list of files to create and clean up"""

        quoted_pipe_names = " ".join(map(shlex.quote, pipe_names))

        self.setup(f"""
            rm -f {quoted_pipe_names}
            mkfifo {quoted_pipe_names}
            cleanup_named_pipes() {{
                rm -f {quoted_pipe_names}
            }}
            trap cleanup_named_pipes EXIT
        """)

    def build_command(
        self, script_name: str, rest_of_script: str | None, after_script: str | None
    ) -> list[str]:
        """
        Constructs the shell command to execute the script with the given arguments.

        Args:
            script_name (str): The name of the script to execute.
            rest_of_script (str): Additional arguments or options to pass to the script.

        Returns:
            list: The constructed shell command as a list of strings.
        """

        command_to_run_script = (
            f"{self.language.command(script_name)} {rest_of_script}".strip()
        )

        if len(self.all_setup_pairs) == 0 and after_script is None:
            command = command_to_run_script
        else:
            after_commands = [dedent(after_script)] if after_script else []

            command = (
                "\n\n".join(
                    [
                        "",
                        *self.prepare_commands,
                        command_to_run_script,
                        *after_commands,
                        *self.cleanup_commands,
                    ]
                )
                + "\n"
            )

        print_command("run in local shell", command)

        return ["/bin/sh", "-c", command]

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
            check=False,  # explicitly define the value for 'check'
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

    def run(self, script_name: str, rest_of_script="", *, after=None, interactive=False):
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

        command = self.build_command(script_name, rest_of_script, after)

        print_command("run in docker", " ".join(map(shlex.quote, command)))

        if interactive:
            script_process = self._run_interactive(command)
        else:
            script_process = self._run(command)

        self.output = script_process.stdout
        self.stdout = script_process.stdout
        self.stderr = script_process.stderr

    def cleanup(self):
        """Cleanup any files created by the script"""

    @property
    def cwd(self) -> str | None:
        """Docker doesn't need this"""
        raise NotImplementedError


class DockerRunner(ScriptRunner):
    """Runner that runs the script in a docker container"""

    image: str

    def __init__(self, language, image):
        super().__init__(language)
        self.image = image

    def build_command(self, *command_args):
        """Build the command to run the script in docker"""
        shell_command = super().build_command(*command_args)

        return ["docker", "run", "--rm", "-i", self.image, *shell_command]

    @property
    def cwd(self) -> str | None:
        """Docker doesn't need this"""
        return None


class LocalRunner(ScriptRunner):
    """Runner that runs the script locally by cd'ing into the language directory
    and running the script"""

    @property
    def cwd(self):
        """Use the directory with named after the language"""
        return self.language.name

    def cleanup(self):
        for file_name in self.files:
            Path(Path(self.cwd, file_name)).unlink(missing_ok=True)


class DockerBuilder:
    """Builds docker images"""

    def print_build_logs(self, logs):
        """Prints the build logs"""
        for chunk in logs:
            if stdout_chunk := chunk.get("stream"):
                print(stdout_chunk, end="")

    def __init__(self, early_bird_locker: EarlyBirdLocker):
        self.docker_client = docker.from_env()
        self.early_bird_locker = early_bird_locker

    def build(self, build_context: str, image_name: str):
        """Builds the docker image, given the build context and image name"""
        print(f"Building docker image {image_name} from {build_context}\n")
        logs = []
        try:
            _, logs = self.docker_client.images.build(
                path=build_context,
                tag=image_name,
                rm=True,
            )
            print("Build succeeded:\n")
            self.print_build_logs(logs)
        except docker.errors.BuildError as e:
            print("Build failed:\n")
            print(e.msg)
            self.print_build_logs(e.build_log)
            raise e

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
        result = self.early_bird_locker.acquire(
            image_name, do_work=lambda: self.build(build_context, image_name)
        )

        match result:
            case ("success", _):
                return image_name
            case ("exception", e):
                raise e
            case ("early-bird-failed", e_name, e_str, e_args):
                pytest.xfail(
                    f"Building docker image {image_name} failed in:\n"
                    + f"{e_name}: {e_str} {e_args}",
                )
            case _:
                raise RuntimeError(f"Unexpected result from early bird lock: {result}")

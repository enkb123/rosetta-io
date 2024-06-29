import json
import os.path
import subprocess
import sys
from abc import ABC
from dataclasses import dataclass
from typing import IO

import docker
import pytest

from locking import early_bird_lock


def expected_read_file_output():
    """Result of reading/capitalizing example input file"""
    expected = ""
    i = 1
    with open('./python/hihello.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            expected += f"{i} {line.upper()}"
            i += 1
    return expected


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
        return f'{script_name}{self.script_ext}'

    def command(self, test_name):
        """Return the shell command that executes the script

        e.g. for Python, this returns "python null_char.py"
        and for R, this returns "Rscript null_char.R"
        """
        return f'{self.interpreter} {self.script_file_name(test_name)}'

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


# pylint: disable=missing-class-docstring

class Python(Language):
    name = 'python'
    interpreter = 'python'
    script_ext = '.py'

class Ruby(Language):
    name = 'ruby'
    interpreter = 'ruby'
    script_ext = '.rb'

class JavaScript(Language):
    name = 'javascript'
    interpreter = 'node'
    script_ext = '.mjs'

class Perl(Language):
    name = 'perl'
    interpreter = 'perl'
    script_ext = '.pl'

class Php(Language):
    name = 'php'
    interpreter = 'php'
    script_ext = '.php'

class R(Language):
    name = 'r'
    interpreter = 'Rscript'
    script_ext = '.R'

class Java(Language):
    name = 'java'
    interpreter = 'java'
    script_ext = '.java'

# pylint: enable=missing-class-docstring

LANGUAGES = [
    Python(),
    Ruby(),
    JavaScript(),
    Php(),
    R(),
    Perl(),
    Java(),
]

@pytest.fixture(params=LANGUAGES, ids=[x.name for x in LANGUAGES])
def language(request):
    """Parametrized fixture with each of the classes in LANGUAGES"""
    return request.param

@pytest.fixture
def docker_client() -> docker.DockerClient:
    """Fixture for a docker client singleton"""
    return docker.from_env()

@pytest.fixture
def once_per_test_suite_run(tmp_path_factory, testrun_uid, worker_id):
    """Fixture that provides a context manager for a lock that is only allowed
    to be acquired once per test suite run"""

    def once_per_this_test_run(*lock_keys):
        return early_bird_lock(
            tmp_path_factory.getbasetemp().parent,
            testrun_uid, *lock_keys,
            worker_id=worker_id
        )
    return once_per_this_test_run

@pytest.fixture
# pylint: disable-next=redefined-outer-name
def docker_image(docker_client: docker.DockerClient, once_per_test_suite_run, language) -> str:
    """Fixture that returns the image name to use for running the script under test, but first
    ensures that the image is built if it is not already.

    Uses the `once_per_test_suite_run` fixture to ensure that the image is only
    built once per test suite run, even for multiple workers.
    """

    image_name = f'{language.name}-rosetta'
    build_context = f'./{language.name}/'

    # Only allow the first pytest-xdist worker that gets here to build the
    # image. Otherwise, they will all try to build it and clobber each other.
    with once_per_test_suite_run("build-image", image_name) as should_build:
        # should_build will be True if this is the the first worker to get here, otherwise False
        if should_build:
            _, logs = docker_client.images.build(path=build_context, tag=image_name)
            for chunk in logs:
                if (stdout_chunk := chunk.get('stream')):
                    print(stdout_chunk, end="")

    return image_name

@dataclass
class ScriptRunner(ABC):
    """Class that handles script execution"""

    image: str
    language: Language
    is_local: bool = False
    container: docker.models.containers.Container = None
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
        return ['/bin/sh', '-c', f'{self.language.command(script_name)} {rest_of_script}']

    @property
    def subprocess_params(self):
        """
        Constructs and returns the parameters for subprocess calls.

        Returns:
            dict: Dictionary of parameters to be used in subprocess calls.
        """
        return dict(
            cwd=self.cwd,
            text=True, # treat standard streams as text, not bytes
            bufsize=1, # set 1 for line buffering, so buffer is flushed when encountering `\n`
        )

    def _run(self, command):
        completed_process = subprocess.run(command,
            capture_output=True, # wait for script to complete
            check=True, # explicitly define the value for 'check'
            **self.subprocess_params
        )
        print(completed_process.stderr, file = sys.stderr)
        return completed_process

    def _run_interactive(self, command):
        running_process = subprocess.Popen( command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            **self.subprocess_params
        )
        self.stdin = running_process.stdin
        return running_process

    def run(self, script_name, rest_of_script = '', interactive = False):
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

    @property
    def cwd(self):
        """Working directory to use when running the script

        Only used when running locally, i.e. not in docker.
        """
        return self.language.name if self.is_local else None


@pytest.fixture
def is_local(request):
    """Fixture that returns True if the test is marked as local, False otherwise"""
    return 'local' in map(lambda m: m.name, request.node.iter_markers())


class DockerRunner(ScriptRunner):
    """Runner that runs the script in a docker container"""

    def build_command(self, *command_args):
        """Build the command to run the script in docker"""
        return ['docker', 'run', '-i', self.image, *super().build_command(*command_args)]

    def clean_up(self):
        """Clean up the docker container, if it was created."""

        # i.e. if the test called `script.run(...)`, which it may not have if it
        # is skipped or failed before creating the container
        if self.container:

            self.container.stop()
            self.container.remove()


class LocalRunner(ScriptRunner):
    """Runner that runs the script locally by cd'ing into the language directory
    and running the script"""

    def clean_up(self):
        """Clean up is not needed for local runner"""

# pylint: disable=redefined-outer-name

@pytest.fixture
def script(docker_image, language, is_local):
    """Fixture that provides a Runner instance"""
    RunnerClass = LocalRunner if is_local else DockerRunner
    runner = RunnerClass(docker_image, language, is_local)

    yield runner
    runner.clean_up()


def test_null_char(script):
    """Test outputing a null character"""
    script.run("null_char")
    assert script.output == 'Hello World \x00\n'



def test_stdin(script):
    """Check that input is read from stdin, line by line.
    The script executed in the docker container accepts a text file as input,
    reads each line, capitalizes it, then prints it out.
    """
    script.run("stdin", "< hihello.txt")
    assert script.output == expected_read_file_output()



def test_read_file(script):
    """Check that a file is read line by line, when file path is given
    as command line argument
    """
    script.run("read_file", "hihello.txt")
    assert script.output == expected_read_file_output()



def test_arguments(script):
    """Test that args can be passed to script"""
    script.run("arguments", '"Argument Number 1"')
    assert script.output == 'argument number 1\n'


def test_read_json_file(script, language):
    """Test that a JSON file is read correctly"""
    # get expected output
    with open(f"{language.name}/person-records.json", "r", encoding="utf-8") as file:
        people = json.load(file)

    expected = "".join(
        f"Hello, {person['age']} year old {person['first_name']}\n" for person in people
    )

    script.run("read_json_file", 'person-records.json')
    assert script.output == expected


def test_write_file(script):
    """Test that a script, given a path to a file, can write to that file"""
    script.run("write_file", 'output.txt "Bob Barker"; cat output.txt')
    assert script.output == "BOB BARKER" # note no new line char


def test_json_array(script):
    """Test that JSON array is parsed correctly"""
    # Write string args as an array of strings to stdout
    script.run("json_array", "a b c d")
    assert json.loads(script.output) == ["a", "b", "c", "d"]


def test_json_numbers(script):
    """Test that JSON list of numbers is parsed correctly"""
    # Write to stdout the length of each string argument
    script.run("json_numbers", 'a bc def ghij')
    assert json.loads(script.output) == [1, 2, 3, 4]


def test_json_stdout_object(script):
    """Test that JSON object is parsed correctly"""
    # Write a dict of {arg:length} to stdout
    # include empty string arg to check handling of empty JSON array
    script.run("json_stdout_object", 'a bc def ghij')
    assert json.loads(script.output) == {"a": 1, "bc": 2, "def": 3, "ghij": 4}


def test_json_object_with_array_values(script):
    """Test that a JSON object with arrays as values is parsed correctly"""
    # Write a dict of {arg:[list of arg chars]} to stdout
    # include empty string arg to check handling of empty JSON array
    script.run("json_object_with_array_values", 'a bc def')
    assert json.loads(script.output) == {"a": ["A"], "bc": ["B", "C"], "def": ["D", "E", "F"]}


def test_json_object_array(script):
    """Test that a JSON array made of objects is parsed correctly"""
    # Write an array of [{arg: length of chars},...] to stdout
    script.run("json_object_array", 'a bc def')
    assert json.loads(script.output) == [{"A": 1}, {"BC": 2}, {"DEF": 3}]


def test_json_control_chars(script):
    """Test that control characters and emojis are output in valid JSON
    note: control character "\0" is used by C (and Python) to end strings and so we can't
    pass it as argument in the test string because it will raise "invalid argument" error
    """
    # Pass a single string to the script that includes a control character and emoji
    script.run("json_control_chars", '"hello \n \1 world 🥸"')
    assert json.loads(script.output) == "hello \n \u0001 world 🥸"


def test_decode(script):
    """Test that base64 can be decoded as a string"""
    script.run("decode", 'SGVsbG8sIHdvcmxkIQ==')
    assert script.output == 'Hello, world!\n'


def test_encode(script):
    """Test that a string can be encoded as base64"""
    script.run("encode", '"Hello, world!"')
    assert script.output == 'SGVsbG8sIHdvcmxkIQ==\n'


def test_streaming_stdin(script):
    """Test that streaming stdin can be read line by line and can write to stdout
    without waiting for all lines to arrive"""
    script.run('streaming_stdin', interactive = True)
    # Give input to the script via stdin, one line at a time, and check result
    for i in range(1, 10):
        script.stdin.write(f"line #{i}\n")
        assert script.stdout.readline() == f"LINE #{i}\n"

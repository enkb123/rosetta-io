import sys
import os.path
from typing import IO
import docker
import pytest
import json
import subprocess
from dataclasses import dataclass
from abc import ABC, abstractmethod

from locking import early_bird_lock


def expected_read_file_output():
    """Result of reading/capitalizing example input file"""
    expected = ""
    i = 1
    with open('./python/hihello.txt', 'r') as f:
        for line in f.readlines():
            expected += f"{i} {line.upper()}"
            i += 1
    return expected


class Language(ABC):
    name: str
    interpreter: str
    script_ext: str

    # def local_script_location(self, script_name):
    #     return os.path.join()
    def script_file_name(self, script_name):
        return f'{script_name}{self.script_ext}'

    def command(self, test_name):
        return f'{self.interpreter} {self.script_file_name(test_name)}'

    @property
    def directory(self):
        return self.name

    def script_local_file(self, script_name):
        return os.path.join(self.directory, self.script_file_name(script_name))


class Python(Language):
    name = 'python'
    # e.g. call the 'null_char' test via `python null_char.py`
    interpreter = 'python'
    script_ext = '.py'

class Ruby(Language):
    name = 'ruby'
    interpreter = 'ruby'
    script_ext = '.rb'

class JavaScript(Language):
    name = 'javascript'
    # e.g. call the 'null_char' test via `node null_char.mjs`
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

class Bash3(Language):
    name = 'bash3'
    interpreter = 'bash'
    script_ext = '.sh'

# List of language classes with which to parametrize tests
LANGUAGES = [Python(), Ruby(), JavaScript(), Php(), R(), Perl(), Java(), Bash3()]

@pytest.fixture(params=LANGUAGES, ids=[x.name for x in LANGUAGES])
def language(request):
    return request.param

@pytest.fixture
def docker_client() -> docker.DockerClient:
    return docker.from_env()

@pytest.fixture
def once_per_test_suite_run(tmp_path_factory, testrun_uid, worker_id):
    def once_per_this_test_run(*lock_keys):
        return early_bird_lock(
            tmp_path_factory.getbasetemp().parent,
            testrun_uid, *lock_keys,
            worker_id=worker_id
        )
    return once_per_this_test_run

@pytest.fixture
def docker_image(docker_client: docker.DockerClient, once_per_test_suite_run, language) -> str:
    """Returns the image name which is all we need for using it, but first ensures that the image is built"""

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
class Runner:
    image: str
    language: Language
    is_local: bool = False
    container: docker.models.containers.Container = None
    output: str = None
    stdin: IO[str] = None
    stdout: IO[str] = None
    stderr: IO[str] = None

    def build_command(self, script_name, rest_of_script):
        return ['/bin/sh', '-c', f'{self.language.command(script_name)} {rest_of_script}']

    @property
    def subprocess_params(self):
        return dict(
            cwd=self.cwd,
            text=True, # treat standard streams as text, not bytes
            bufsize=1, # set 1 for line buffering, so buffer is flushed when encountering `\n`
        )

    def _run(self, command):
        script = subprocess.run(command,
            capture_output=True, # wait for script to complete
            **self.subprocess_params
        )
        print(script.stderr, file = sys.stderr)
        return script

    def _run_interactive(self, command):
        script = subprocess.Popen( command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            **self.subprocess_params
        )
        self.stdin = script.stdin
        return script

    def run(self, script_name, rest_of_script = '', interactive = False):

        if not os.path.isfile(self.language.script_local_file(script_name)):
            pytest.skip(f"Script {repr(script_name)} is not implemented for language {repr(self.language.name)}")

        command = self.build_command(script_name, rest_of_script)

        print("command:", command)

        if interactive:
            script = self._run_interactive(command)
        else:
            script = self._run(command)

        self.output = script.stdout
        self.stdout = script.stdout
        self.stderr = script.stderr

    @property
    def cwd(self):
        return self.language.name if self.is_local else None


@pytest.fixture
def is_local(request):
    return 'local' in map(lambda m: m.name, request.node.iter_markers())


class DockerRunner(Runner):
    def build_command(self, script_name, rest_of_script):
        return ['docker', 'run', '-i', self.image, *super(DockerRunner, self).build_command(script_name, rest_of_script)]

    def clean_up(self):
        if self.container: # i.e. if the test called `script.run(...)`
            self.container.stop()
            self.container.remove()


class LocalRunner(Runner):
    def clean_up(self):
        pass


@pytest.fixture
def script(docker_image, language, is_local):
    RunnerClass = LocalRunner if is_local else DockerRunner
    runner = RunnerClass(docker_image, language, is_local)

    yield runner
    runner.clean_up()


class TestNullChar:
    def test_null_char(self, script):
        script.run("null_char")
        assert script.output == 'Hello World \x00\n'


class TestStdIn:
    """Check that input is read from stdin, line by line.
    The script executed in the docker container accepts a text file as input,
    reads each line, capitalizes it, then prints it out.
    """
    def test_stdin(self, script):
        script.run("stdin", "< hihello.txt")
        assert script.output == expected_read_file_output()


class TestReadFile:
    """Check that a file is read line by line, when file path is given
    as command line argument
    """
    def test_read_file(self, script):
        script.run("read_file", "hihello.txt")
        assert script.output == expected_read_file_output()


class TestArgs:
    """Test that args can be passed to script"""
    def test_arguments(self, script):
        script.run("arguments", '"Argument Number 1"')
        assert script.output == 'argument number 1\n'


class TestReadJsonFile:
    """Test that a JSON file is read correctly"""
    def test_read_json_file(self, script, language):
        # get expected output
        file_path = f"{language.name}/person-records.json"
        with open(file_path, "r") as file:
            people = json.load(file)
        expected = "".join(f"Hello, {person['age']} year old {person['first_name']}\n" for person in people)

        script.run("read_json_file", 'person-records.json')
        assert script.output == expected


class TestWriteFile:
    """Test that a script, given a path to a file, can write to that file"""
    def test_write_file(self, script):
        script.run("write_file", 'output.txt "Bob Barker"; cat output.txt')
        assert script.output == "BOB BARKER" # note no new line char


class TestWriteJsonToStdout:
    def test_json_array(self, script):
        """Test that JSON array is parsed correctly"""
        # Write string args as an array of strings to stdout
        script.run("json_array", "a b c d")
        assert json.loads(script.output) == ["a", "b", "c", "d"]

    def test_json_numbers(self, script):
        """Test that JSON list of numbers is parsed correctly"""
        # Write to stdout the length of each string argument
        script.run("json_numbers", 'a bc def ghij')
        assert json.loads(script.output) == [1, 2, 3, 4]

    def test_json_stdout_object(self, script):
        """Test that JSON object is parsed correctly"""
        # Write a dict of {arg:length} to stdout
        # include empty string arg to check handling of empty JSON array
        script.run("json_stdout_object", 'a bc def ghij')
        assert json.loads(script.output) == {"a": 1, "bc": 2, "def": 3, "ghij": 4}

    def test_json_object_with_array_values(self, script):
        """Test that a JSON object with arrays as values is parsed correctly"""
        # Write a dict of {arg:[list of arg chars]} to stdout
        # include empty string arg to check handling of empty JSON array
        script.run("json_object_with_array_values", 'a bc def')
        assert json.loads(script.output) == {"a": ["A"], "bc": ["B", "C"], "def": ["D", "E", "F"]}

    def test_json_object_array(self, script):
        """Test that a JSON array made of objects is parsed correctly"""
        # Write an array of [{arg: length of chars},...] to stdout
        script.run("json_object_array", 'a bc def')
        assert json.loads(script.output) == [{"A": 1}, {"BC": 2}, {"DEF": 3}]

    def test_json_control_chars(self, script):
        """Test that control characters and emojis are output in valid JSON
        note: control character "\0" is used by C (and Python) to end strings and so we can't
        pass it as argument in the test string because it will raise "invalid argument" error
        """
        # Pass a single string to the script that includes a control character and emoji
        script.run("json_control_chars", '"hello \n \1 world 🥸"')
        assert json.loads(script.output) == "hello \n \u0001 world 🥸"


class TestDecodeBase64:
    """Test that base64 can be decoded as a string"""
    def test_decode(self, script):
        script.run("decode", 'SGVsbG8sIHdvcmxkIQ==')
        assert script.output == 'Hello, world!\n'


class TestEncodeBase64:
    """Test that a string can be encoded as base64"""
    def test_encode(self, script):
        script.run("encode", '"Hello, world!"')
        assert script.output == 'SGVsbG8sIHdvcmxkIQ==\n'


class TestStreamingStdin:
    """Test that streaming stdin can be read line by line and can write to stdout
    without waiting for all lines to arrive"""
    def test_streaming_stdin(self, script):
        script.run('streaming_stdin', interactive = True)
        # Give input to the script via stdin, one line at a time, and check result
        for i in range(1, 10):
            script.stdin.write(f"line #{i}\n")
            assert script.stdout.readline() == f"LINE #{i}\n"

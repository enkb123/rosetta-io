# pylint: disable=redefined-outer-name, missing-class-docstring

import json
from re import sub

import pytest

# pylint: disable-next=unused-import
from test_helpers import (
    DockerBuilder,
    DockerRunner,
    EarlyBirdLocker,
    Language,
    LocalRunner,
    ScriptRunner,
    dedent,
    once_per_test_suite_run,  # noqa: F401
)


class Python(Language):
    name = "python"
    interpreter = "python"
    script_ext = ".py"


class Ruby(Language):
    name = "ruby"
    interpreter = "ruby"
    script_ext = ".rb"


class JavaScript(Language):
    name = "javascript"
    interpreter = "node"
    script_ext = ".mjs"


class Perl(Language):
    name = "perl"
    interpreter = "perl"
    script_ext = ".pl"


class Php(Language):
    name = "php"
    interpreter = "php"
    script_ext = ".php"


class R(Language):
    name = "r"
    interpreter = "Rscript"
    script_ext = ".R"


class Java(Language):
    name = 'java'
    interpreter = 'java'
    script_ext = '.java'

    def script_file_name(self, script_name):
        return f'{self.camel_case(script_name)}{self.script_ext}'

    def camel_case(self, s):
        # Use regular expression substitution to replace underscores and hyphens with spaces,
        # then title case the string (capitalize the first letter of each word), and remove spaces
        return sub(r"(_|-)+", " ", s).title().replace(" ", "")


class Bash3(Language):
    name = 'bash3'
    interpreter = 'bash'
    script_ext = '.sh'


class Bash5(Bash3):
    name = 'bash5'


LANGUAGES = [
    Python(),
    Ruby(),
    JavaScript(),
    Php(),
    R(),
    Perl(),
    Java(),
    Bash3(),
    Bash5(),
]


@pytest.fixture(params=LANGUAGES, ids=[x.name for x in LANGUAGES])
def language(request: pytest.FixtureRequest):
    """Parametrized fixture with each of the classes in LANGUAGES"""
    return request.param


@pytest.fixture
def is_local(request: pytest.FixtureRequest):
    """Fixture that returns True if the test is marked as local, False otherwise"""
    markers_names = map(lambda m: m.name, request.node.iter_markers())
    return "local" in markers_names


@pytest.fixture
def docker_builder(once_per_test_suite_run: EarlyBirdLocker) -> DockerBuilder:  # noqa: F811
    """Fixture for a docker client singleton"""
    return DockerBuilder(once_per_test_suite_run)


@pytest.fixture
def script(docker_builder: DockerBuilder, language: Language, is_local: bool):
    """Fixture that provides a ScriptRunner instance"""
    if is_local:
        runner = LocalRunner(language)
    else:
        runner = DockerRunner(language, docker_builder.docker_image(language.name))

    yield runner

    runner.cleanup()


def test_null_char(script: ScriptRunner):
    """Test outputing a null character"""
    script.run("null_char")
    assert script.output == "Hello World \x00\n"


def test_stdin(script: ScriptRunner):
    """Check that input is read from stdin, line by line.
    The script executed in the docker container accepts a text file as input,
    reads each line, capitalizes it, then prints it out.
    """

    script.files["hihello-stdin.txt"] = dedent("""
        hi
        hello
        how are you
    """)

    script.run("stdin", "< hihello-stdin.txt")

    assert script.output == dedent("""
        1 HI
        2 HELLO
        3 HOW ARE YOU
    """)


def test_read_file(script: ScriptRunner):
    """Check that a file is read line by line, when file path is given
    as command line argument
    """
    script.files["hihello-read-file.txt"] = dedent("""
        hi
        hello
        how are you
    """)

    script.run("read_file", "hihello-read-file.txt")

    assert script.output == dedent("""
        1 HI
        2 HELLO
        3 HOW ARE YOU
    """)


def test_arguments(script: ScriptRunner):
    """Test that args can be passed to script"""
    script.run("arguments", '"Argument Number 1"')
    assert script.output == "argument number 1\n"


def test_read_json_file(script: ScriptRunner):
    """Test that a JSON file is read correctly"""

    script.files["people-read-json-file.json"] = json.dumps(
        [
            {"first_name": "Bob", "last_name": "Barker", "age": 84},
            {"first_name": "Tina", "last_name": "Turner", "age": 67},
            {"first_name": "Steven", "last_name": "Sagal", "age": 98},
        ]
    )

    script.run("read_json_file", "people-read-json-file.json")

    assert script.output == dedent("""
        Hello, 84 year old Bob
        Hello, 67 year old Tina
        Hello, 98 year old Steven
    """)


def test_write_file(script: ScriptRunner):
    """Test that a script, given a path to a file, can write to that file"""
    script.run("write_file", 'output.txt "Bob Barker"; cat output.txt')
    assert script.output == "BOB BARKER"  # note no new line char


def test_json_array(script: ScriptRunner):
    """Test that JSON array is parsed correctly"""
    # Write string args as an array of strings to stdout
    script.run("json_array", "a b c d")
    assert json.loads(script.output) == ["a", "b", "c", "d"]


def test_json_numbers(script: ScriptRunner):
    """Test that JSON list of numbers is parsed correctly"""
    # Write to stdout the length of each string argument
    script.run("json_numbers", "a bc def ghij")
    assert json.loads(script.output) == [1, 2, 3, 4]


def test_json_stdout_object(script: ScriptRunner):
    """Test that JSON object is parsed correctly"""
    # Write a dict of {arg:length} to stdout
    # include empty string arg to check handling of empty JSON array
    script.run("json_stdout_object", "a bc def ghij")
    assert json.loads(script.output) == {"a": 1, "bc": 2, "def": 3, "ghij": 4}


def test_json_object_with_array_values(script: ScriptRunner):
    """Test that a JSON object with arrays as values is parsed correctly"""
    # Write a dict of {arg:[list of arg chars]} to stdout
    # include empty string arg to check handling of empty JSON array
    script.run("json_object_with_array_values", "a bc def")
    assert json.loads(script.output) == {
        "a": ["A"],
        "bc": ["B", "C"],
        "def": ["D", "E", "F"],
    }


def test_json_object_array(script: ScriptRunner):
    """Test that a JSON array made of objects is parsed correctly"""
    # Write an array of [{arg: length of chars},...] to stdout
    script.run("json_object_array", "a bc def")
    assert json.loads(script.output) == [{"A": 1}, {"BC": 2}, {"DEF": 3}]


def test_json_control_chars(script: ScriptRunner):
    """Test that control characters and emojis are output in valid JSON
    note: control character "\0" is used by C (and Python) to end strings and so we can't
    pass it as argument in the test string because it will raise "invalid argument" error
    """
    # Pass a single string to the script that includes a control character and emoji
    script.run("json_control_chars", '"hello \n \1 world 🥸"')
    assert json.loads(script.output) == "hello \n \u0001 world 🥸"


def test_base64_decode(script: ScriptRunner):
    """Test that base64 can be decoded as a string"""
    script.run("decode", "SGVsbG8sIHdvcmxkIQ==")
    assert script.output == "Hello, world!\n"


def test_base64_encode(script: ScriptRunner):
    """Test that a string can be encoded as base64"""
    script.run("encode", '"Hello, world!"')
    assert script.output == "SGVsbG8sIHdvcmxkIQ==\n"


def test_streaming_stdin(script: ScriptRunner):
    """Test that streaming stdin can be read line by line and can write to stdout
    without waiting for all lines to arrive"""
    script.run("streaming_stdin", interactive=True)
    # Give input to the script via stdin, one line at a time, and check result
    for i in range(1, 10):
        script.stdin.write(f"line #{i}\n")
        assert script.stdout.readline() == f"LINE #{i}\n"

# pylint: disable=redefined-outer-name, missing-class-docstring

import json
import os


import pytest

# pylint: disable-next=unused-import
from test_helpers import (
    DockerBuilder,
    DockerRunner,
    EarlyBirdLocker,
    Language,
    LocalRunner,
    ScriptRunner,
    assert_string_match,
    dedent,
    camel_case,
    markers,
    once_per_test_suite_run, # noqa: F401
    script_name_of_test_case,
)


class Python(Language):
    name = 'python'
    human_name = 'Python'
    interpreter = 'python'
    script_ext = '.py'
    syntax_highlighting = 'python'


class Ruby(Language):
    name = 'ruby'
    human_name = 'Ruby'
    interpreter = 'ruby'
    script_ext = '.rb'
    syntax_highlighting = 'ruby'


class Nodejs(Language):
    name = 'nodejs'
    human_name = 'Nodejs'
    interpreter = 'node'
    script_ext = '.mjs'
    syntax_highlighting = 'javascript'


class Deno(Nodejs):
    name = 'deno'
    human_name = 'Deno'
    interpreter = 'deno run --allow-read --allow-write'
    script_ext = '.mjs'
    syntax_highlighting = 'javascript'
    icon_id = 'denojs'


class Perl(Language):
    name = 'perl'
    human_name = 'Perl'
    interpreter = 'perl'
    script_ext = '.pl'
    syntax_highlighting = 'perl'


class Php(Language):
    name = 'php'
    human_name = 'Php'
    interpreter = 'php'
    script_ext = '.php'
    syntax_highlighting = 'php'


class R(Language):
    name = 'r'
    human_name = 'R'
    interpreter = 'Rscript'
    script_ext = '.R'
    syntax_highlighting = 'r'


class Java(Language):
    name = 'java'
    human_name = 'Java'
    interpreter = 'java'
    script_ext = '.java'
    syntax_highlighting = 'java'

    def script_file_name(self, script_name):
        return f'{camel_case(script_name)}{self.script_ext}'


class Bash3(Language):
    name = 'bash3'
    human_name = 'Bash 3'
    interpreter = 'bash'
    script_ext = '.sh'
    syntax_highlighting = 'bash'
    icon_id = 'bash'


class Bash5(Bash3):
    name = 'bash5'
    human_name = 'Bash 5'
    icon_id = 'bash'


class Lua(Language):
    name = 'lua'
    human_name = 'Lua'
    interpreter = 'lua'
    script_ext = '.lua'
    syntax_highlighting = 'lua'


class CSharp(Language):
    """C# language
    Compiles *all* the scripts in the csharp directory, so if one of them fails
    to compile, none of the others will compile.

    Also, because .NET doesn't make it easy to build a single executable per script,
    the Program.cs file is compiled into a single executable, and then each script is run by passing
    the script name as the first argument. See Program.cs for details.
    """
    name = 'csharp'
    script_ext = '.cs'
    human_name = 'C#'
    syntax_highlighting = 'csharp'

    def command(self, test_name):
        return f"dotnet run {test_name}"

    def script_file_name(self, script_name):
        return f'{camel_case(script_name)}{self.script_ext}'


class Golang(Language):
    name = 'golang'
    human_name  = 'Go'
    interpreter = 'go run'
    script_ext = '.go'
    syntax_highlighting = 'go'
    icon_id = 'go'


class Swift(Language):
    name = 'swift'
    human_name = 'Swift'
    interpreter = 'swift'
    script_ext = '.swift'
    syntax_highlighting = 'swift'


class Raku(Language):
    name = 'raku'
    human_name = 'Raku'
    interpreter = 'raku'
    script_ext = '.raku'
    syntax_highlighting = 'raku'


class Rust(Language):
    name = 'rust'
    human_name = 'Rust'
    interpreter = 'cargo script'
    script_ext = '.rs'
    syntax_highlighting = 'rust'


LANGUAGES = [
    Python(),
    Ruby(),
    Nodejs(),
    Deno(),
    Php(),
    R(),
    Perl(),
    Java(),
    Bash3(),
    Bash5(),
    Lua(),
    CSharp(),
    Golang(),
    Swift(),
    Raku(),
    Rust(),
]


@pytest.fixture(params=LANGUAGES, ids=[x.name for x in LANGUAGES])
def language(request: pytest.FixtureRequest):
    """Parametrized fixture with each of the classes in LANGUAGES"""
    return request.param


@pytest.fixture
def is_local(request: pytest.FixtureRequest):
    """Fixture that returns True if the test is marked as local, False otherwise"""
    if os.environ.get("TEST_LOCAL", "false").lower() in ("true", "1", "yes"):
        return True
    return "local" in markers(request.node)


@pytest.fixture
def docker_builder(once_per_test_suite_run: EarlyBirdLocker) -> DockerBuilder:  # noqa: F811
    """Fixture for a docker client singleton"""
    return DockerBuilder(once_per_test_suite_run)


@pytest.fixture
def script(request: pytest.FixtureRequest, docker_builder: DockerBuilder, language: Language, is_local: bool):
    """Fixture that provides a ScriptRunner instance"""

    script_name = script_name_of_test_case(request.node)

    if is_local:
        runner = LocalRunner(script_name, language)
    else:
        runner = DockerRunner(script_name, language, docker_builder.docker_image(language))

    yield runner

    runner.cleanup()


def test_null_char(script: ScriptRunner):
    """Output a null character

    See https://en.wikipedia.org/wiki/Null_character
    """
    script.run()
    assert_string_match(script.output, "Hello World \x00")


def test_stdin(script: ScriptRunner):
    """Read from stdin line by line"""

    script.run(dedent("""<<EOF
        hi
        hello
        how are you
        EOF
    """))

    assert_string_match(script.output, dedent("""
        line: hi
        line: hello
        line: how are you
    """))


def test_read_file(script: ScriptRunner):
    """Read a file line by line"""

    script.files["my-text-file.txt"] = dedent("""
        hi
        hello
        how are you
    """)

    script.run()

    assert_string_match(script.output, dedent("""
        line: hi
        line: hello
        line: how are you
    """))



def test_arguments(script: ScriptRunner):
    """Read command line arguments"""
    script.run('"Argument Number 1" "Command line arg 2"')
    assert_string_match(script.output, dedent("""
        1st argument: Argument Number 1
        2nd argument: Command line arg 2
    """))


def test_read_json_file(script: ScriptRunner):
    """Read and parse a JSON file"""

    script.files["people.json"] = json.dumps(
        [
            {"first_name": "Bob", "last_name": "Barker", "age": 84},
            {"first_name": "Tina", "last_name": "Turner", "age": 67},
            {"first_name": "Steven", "last_name": "Sagal", "age": 98},
        ]
    )

    script.run()

    assert_string_match(script.output, dedent("""
        Hello, 84 year old Bob
        Hello, 67 year old Tina
        Hello, 98 year old Steven
    """))


def test_write_to_text_file(script: ScriptRunner):
    """Write to a text file"""
    script.files["output.txt"] = "THIS SHOULD BE OVERWRITTEN"

    script.run(after="cat output.txt && rm output.txt")

    assert_string_match(script.output, "Hello World!")


def test_json_outputting_data(script: ScriptRunner):
    """Create and output JSON"""

    script.run()

    data = [json.loads(line) for line in script.output.strip().split("\n")]

    assert data == [
        {
            "true": True,
            "false": False,
            "zero": 0,
            "int": 42,
            "float": 3.14,
            "null": None,
            "empty string": "",
            "a string with non-ascii characters": "hello \n \0 \u0001 world 🥸",
        },
        {
            "array of strings": ["abc", "def", "ghi", "jkl"],
            "array of numbers": [13, 42, 9000, -7],
            "array of nothing": [],
            "array of mixed": [13, "def", None, False, ["a"], { "o": 1}],
            "array of objects": [
                { "name": "Bob Barker", "age": 84 },
                { "address1": "123 Main St", "address2": "Apt 1" },
            ],
            "array of arrays": [
                ["a", "b", "c"],
                ["d", "e", "f"],
            ],
        },
        {
            "objects": { "nested": { "objects": { "are": "supported" } } },
        }
    ]


def test_json_array(script: ScriptRunner):
    """Create and output a JSON array of strings"""

    script.run("a b c d")
    assert json.loads(script.output) == ["a", "b", "c", "d"]


def test_json_numbers(script: ScriptRunner):
    """Create and output a JSON array of numbers"""

    # Write to stdout the length of each string argument
    script.run("a bc def ghij")
    assert json.loads(script.output) == [1, 2, 3, 4]


def test_json_stdout_object(script: ScriptRunner):
    """Create and output a JSON object"""

    # Write a dict of {arg:length} to stdout
    script.run("a bc def ghij")

    assert json.loads(script.output) == {"a": 1, "bc": 2, "def": 3, "ghij": 4}


def test_json_object_with_array_values(script: ScriptRunner):
    """Create and output a JSON object with arrays of strings as values"""

    # Write a dict of {arg:[list of arg chars]} to stdout
    script.run("a bc def")

    assert json.loads(script.output) == {
        "a": ["A"],
        "bc": ["B", "C"],
        "def": ["D", "E", "F"],
    }


def test_json_object_array(script: ScriptRunner):
    """Create and output a JSON array of objects"""

    # Write an array of [{arg: length of chars},...] to stdout
    script.run("a bc def")

    assert json.loads(script.output) == [{"A": 1}, {"BC": 2}, {"DEF": 3}]


def test_json_control_chars(script: ScriptRunner):
    """Test that control characters and emojis are output in valid JSON."""

    # Note: control character "\\0" is used by C (and Python) to end strings and so we can't
    # pass it as argument in the test string because it will raise "invalid argument" error

    # Pass a single string to the script that includes a control character and emoji
    script.run('"hello \n \1 world 🥸"')

    assert json.loads(script.output) == "hello \n \u0001 world 🥸"


@pytest.mark.script(script_name="decode")
def test_base64_decode(script: ScriptRunner):
    """Decode a base64 string"""

    script.run("SGVsbG8sIHdvcmxkIQ==")

    assert_string_match(script.output, "Hello, world!")


@pytest.mark.script(script_name="encode")
def test_base64_encode(script: ScriptRunner):
    """Encode a string as base64"""

    script.run('"Hello, world!"')

    assert_string_match(script.output, "SGVsbG8sIHdvcmxkIQ==")


def test_streaming_stdin(script: ScriptRunner):
    """Read from stdin line by line"""

    # Tests that streaming stdin can be read line by line and can write to
    # stdout without waiting for all lines to arrive
    script.run(interactive=True)

    # Give input to the script via stdin, one line at a time, and check result
    for i in range(1, 10):
        script.stdin.write(f"line #{i}\n")
        assert_string_match(script.stdout.readline(), f"received line #{i}")


@pytest.mark.script(script_name="streaming_pipe_in")
def test_streaming_from_pipe_in(script: ScriptRunner):
    """Read from named pipe line by line"""

    script.add_named_pipe("input.pipe")

    script.run("|| echo ERROR &",
        after="""
            # send input from test runner to the input pipe
            cat > input.pipe

            wait
        """,
        interactive=True,
    )

    for i in range(1, 10):
        script.stdin.write(f"line #{i}\n")
        assert_string_match(script.stdout.readline(), f"LINE #{i}")


def test_write_to_named_pipe(script: ScriptRunner):
    """Write text to a named pipe"""

    script.add_named_pipe("output.pipe")

    script.run('|| echo ERROR &',
        after="""
            cat output.pipe &
            wait
        """,
        interactive=True,
    )
    assert_string_match(script.stdout.readline(), "Hello World!")


def test_streaming_pipe_in_and_out(script: ScriptRunner):
    """Read line by line from a named pipe and write to another named pipe"""

    # Tests that it can process named pipe input and send output one line at a
    # time without waiting for all lines to arrive
    script.add_named_pipe("streaming-in.pipe", "streaming-out.pipe")

    # redirect stdout to stderr so that we can capture it in the test runner if
    # there is an error
    script.run(">&2 || echo ERROR &",
        after="""
            # read from streaming-out.pipe and write it to stdout, which the
            # test runner captures
            cat streaming-out.pipe &

            # takes stdin (input from the test runner) and writes it to
            # streaming-in.pipe
            cat > streaming-in.pipe

            wait
        """,
        interactive=True,
    )

    for i in range(1, 10):
        script.stdin.write(f"line #{i}\n")
        assert_string_match(script.stdout.readline(), f"received line #{i}")

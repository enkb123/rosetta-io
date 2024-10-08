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
    script_test_case_mark,
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
    human_name = 'Javascript (Node.js)'
    interpreter = 'node'
    script_ext = '.mjs'
    syntax_highlighting = 'javascript'


class Deno(Nodejs):
    name = 'deno'
    human_name = 'Javascript (Deno)'
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
    human_name = 'PHP'
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


class Bash(Language):
    name = 'bash'
    human_name = 'Bash'
    interpreter = 'bash'
    script_ext = '.sh'
    syntax_highlighting = 'bash'
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
    Bash(),
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

    mark = script_test_case_mark(request.node)
    script_name = mark["script_name"]

    if is_local:
        runner = LocalRunner(script_name, language, mark)
    else:
        runner = DockerRunner(script_name, language, mark, docker_builder.docker_image(language))

    yield runner

    runner.cleanup()


@pytest.mark.script(
    group="Misc",
    title="Null character",
    assertion=('stdout_match', "Hello World \x00")
)
def test_null_char(script: ScriptRunner):
    """Output a null character to stdout

    See https://en.wikipedia.org/wiki/Null_character
    """
    script.run()
    script.assert_output()


@pytest.mark.script(
    group="Standard I/O",
    title="Standard input",
    stdin=dedent("""
        hi
        hello
        how are you
    """),
    assertion=('stdout_match', dedent("""
        line: hi
        line: hello
        line: how are you
    """)))
def test_stdin(script: ScriptRunner):
    """Read from stdin line by line

    Read one line at a time from stdin and print it.
    This example assumes that all the input on stdin is available at once.
    """

    script.run()
    script.assert_output()

@pytest.mark.script(
    group="File I/O",
    title="Read text file",
    files={"my-text-file.txt": dedent("""
        hi
        hello
        how are you
    """)},
    assertion=('stdout_match', dedent("""
        line: hi
        line: hello
        line: how are you
    """))
)
def test_read_file(script: ScriptRunner):
    """Read a text file line by line

    Read one line at a time from a file called `my-text-file.txt` and print it.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    group="Misc",
    title="Command-line arguments",
    cli_args=["Argument Number 1", "Command line arg 2"],
    assertion=('stdout_match', dedent("""
        1st argument: Argument Number 1
        2nd argument: Command line arg 2
    """))
)
def test_arguments(script: ScriptRunner):
    """Read command line arguments

    Read 2 command line arguments and print them out.
    """
    script.run()
    script.assert_output()


@pytest.mark.script(
    group="JSON",
    title="Parse JSON file",
    files={"people.json": json.dumps(
        [
            {"first_name": "Bob", "last_name": "Barker", "age": 84},
            {"first_name": "Tina", "last_name": "Turner", "age": 67},
            {"first_name": "Steven", "last_name": "Sagal", "age": 98},
        ],
        indent=4
    )},
    assertion=('stdout_match', dedent("""
        Hello, 84 year old Bob
        Hello, 67 year old Tina
        Hello, 98 year old Steven
    """))
)
def test_read_json_file(script: ScriptRunner):
    """Read and parse a JSON file

    Read a JSON file called `people.json` that contains an array of JSON objects.
    For each JSON object, print a greeting.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    group="File I/O",
    title="Write text file",
)
def test_write_to_text_file(script: ScriptRunner):
    """Write to a text file

    Write the string `Hello World!` to a file named `output.txt`.
    """

    # do this here instead of in the mark so that that the website doesn't show this file
    script.files["output.txt"] = "THIS SHOULD BE OVERWRITTEN"

    script.run(after="cat output.txt && rm output.txt")

    # do this here instead of in the mark so that that the website doesn't show this file
    assert_string_match(script.output, "Hello World!")

@pytest.mark.script(
    group="JSON",
    title="Output JSON"
)
def test_json_outputting_data(script: ScriptRunner):
    """Create and output JSON

    Create and output JSON that contains a variety of data types.
    """

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
            "a string with non-ascii characters": "hello \n \u0001 world 🥸",
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

@pytest.mark.script(
    group="JSON",
    title="JSON with null character",
    assertion=('json', "Hello World \0")
)
def test_json_null_char(script: ScriptRunner):
    """Create output JSON with a null character

    In a JSON string the null character is represented as `\\u0000`.

    JSON strings are UTF-8 encoded, so the null character is valid, but
    nevertheless, some JSON parsers cannot handle it.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    group="JSON",
    title="Build JSON array of strings",
    cli_args=["a", "b", "c", "d"],
    assertion=('json', ["a", "b", "c", "d"])
)
def test_json_array(script: ScriptRunner):
    """Create and output a JSON array of strings

    Accept a list of strings as command line arguments.
    Create and output a JSON array of those strings.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    group="JSON",
    title="Build JSON array of numbers",
    cli_args=["a", "bc", "def", "ghij"],
    assertion=('json', [1, 2, 3, 4]),
)
def test_json_numbers(script: ScriptRunner):
    """Create and output a JSON array of numbers

    Accept a list of strings as command line arguments.
    Create and output a JSON array of the *lengths* of the strings.
    """

    # Write to stdout the length of each string argument
    script.run()
    script.assert_output()


@pytest.mark.script(
    group="JSON",
    title="Build JSON object",
    cli_args=["a", "bc", "def", "ghij"],
    assertion=('json', {"a": 1, "bc": 2, "def": 3, "ghij": 4}),
)
def test_json_stdout_object(script: ScriptRunner):
    """Create and output a JSON object

    Accept a list of strings as command line arguments.
    Create and output a JSON object with the strings as keys and their lengths as values.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    group="JSON",
    title="Build JSON object of arrays of strings",
    cli_args=["a", "bc", "def"],
    assertion=('json', {
        "a": ["A"],
        "bc": ["B", "C"],
        "def": ["D", "E", "F"]
    })
)
def test_json_object_with_array_values(script: ScriptRunner):
    """Create and output a JSON object with arrays of strings as values

    Accept a list of strings as command line arguments.
    Create and output a JSON object with the strings as keys and arrays of their characters as values.
    """

    script.run()
    script.assert_output()

@pytest.mark.script(
    group="JSON",
    title="Build JSON array of objects",
    cli_args=["a", "bc", "def"],
    assertion=('json', [{"A": 1}, {"BC": 2}, {"DEF": 3}])
)
def test_json_object_array(script: ScriptRunner):
    """Create and output a JSON array of objects

    Accept a list of strings as command line arguments.
    Create and output a JSON array of objects, one for each strings, where each
    object has a key-value pair where the key is the uppercased string and the
    value is the length of the string.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    group="JSON",
    title="JSON with control characters & emoji",
    cli_args=["hello \n \u0001 world 🥸"],
    assertion=('json', "hello \n \u0001 world 🥸")
)
def test_json_control_chars(script: ScriptRunner):
    """Build and out output a JSON string containing control characters and emojis.

    Receive a string as a command line argument and print it as the JSON string. The string is
    `"hello \\n \\u0001 world 🥸"`.

    See [JSON with null character](../json_null_char) for outputting the Null Character (`\\0`) in a JSON string.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    script_name="decode",
    group="Base64",
    title="Decode Base64",
    cli_args=["SGVsbG8sIHdvcmxkIQ=="],
    assertion=('stdout_match', "Hello, world!")
)
def test_base64_decode(script: ScriptRunner):
    """Decode a base64 string

    Accept a base64 encoded string as a command line argument, decode it, and print it out.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(
    script_name="encode",
    group="Base64",
    title="Encode Base64",
    cli_args=["Hello, world!"],
    assertion=('stdout_match', "SGVsbG8sIHdvcmxkIQ==")
)
def test_base64_encode(script: ScriptRunner):
    """Encode a string as base64

    Accept a string as a command line argument, encode it as Base64, then print it out.
    """

    script.run()
    script.assert_output()


@pytest.mark.script(group="Standard I/O", title="Streaming standard input")
def test_streaming_stdin(script: ScriptRunner):
    """Stream from stdin line by line

    Stream one line at a time from stdin and print it to stdout.

    The test runner for this case will only provide the next line on stdin when the previous line has be printed to stdout.
    This requires either that stdout is unbuffered or that stdout is flushed after each line is written to it.
    Some languages do this automatically, other don't.
    """

    # Tests that streaming stdin can be read line by line and can write to
    # stdout without waiting for all lines to arrive
    script.run(interactive=True)

    # Give input to the script via stdin, one line at a time, and check result
    for i in range(1, 10):
        script.stdin.write(f"line #{i}\n")
        assert_string_match(script.stdout.readline(), f"received line #{i}")


@pytest.mark.script(script_name="streaming_pipe_in", group="Pipe I/O", title="Streaming from named pipe")
def test_streaming_from_pipe_in(script: ScriptRunner):
    """Stream from a named pipe line by line

    Stream one line at a time from a named pipe (named `input.pipe`) and print it to stdout.
    The test runner for this case will only provide the next line on the `input.pipe` when the previous line has be printed to stdout.

    This requires either that stdout is unbuffered or that stdout is flushed after each line is written to it.
    Some languages do this automatically, other don't.
    """

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


@pytest.mark.script(group="Pipe I/O", title="Write to named pipe")
def test_write_to_named_pipe(script: ScriptRunner):
    """Write text to a named pipe

    Write `Hello World!` to a named pipe (named `output.pipe`).

    When writing to named pipes, the program does not need to know it's a pipe,
    but can treat it as a regular file when writing to it.
    """

    script.add_named_pipe("output.pipe")

    script.run('|| echo ERROR &',
        after="""
            cat output.pipe &
            wait
        """,
        interactive=True,
    )
    assert_string_match(script.stdout.readline(), "Hello World!")


@pytest.mark.script(group="Pipe I/O", title="Streaming to and from named pipes")
def test_streaming_pipe_in_and_out(script: ScriptRunner):
    """Stream lines from a named pipe, write to another named pipe

    Stream one line at a time from a named pipe (named `streaming-in.pipe`) and
    print it to another named pipe (named `streaming-out.pipe`).

    The test runner for this case will only provide the next line on stdin when the previous line has be printed to stdout.
    This requires either that stdout is unbuffered or that stdout is flushed after each line is written to it.
    Some languages do this automatically, other don't.
    """

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

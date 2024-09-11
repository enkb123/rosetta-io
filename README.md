https://rosetta-io.netlify.app/

# I/O ergonomics of popular languages

Working examples of how popular languages handle basic I/O and common serialization formats.

The examples are validated via a test suite that runs the examples in Docker and verifies expected behavior.

This project is not currently meant to be exhaustive in terms of languages, operating systems and I/O operations. The languages and I/O operations, etc are prioritized to support a commercial devtool product currently in stealth mode. That being said, contributions are very welcome.

The name `rosetta-io` is an hommage to [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code) but is not affiliated.

## Languages covered

| Language            | Status      |
| ------------------- | ----------- |
| Python 3            | ✅          |
| Ruby                | ✅          |
| Javascript, Node.js | ✅          |
| PHP                 | ✅          |
| R                   | ✅          |
| Deno                | ✅          |
| Perl                | ✅          |
| Java                | ✅          |
| Bash 3              | ✅          |
| Bash 5              | ✅          |
| Lua                 | ✅          |
| C#                  | ✅          |
| Golang              | ✅          |
| Swift               | ✅          |
| Raku                | ✅          |
| Rust                | ✅          |
| …                   |             |

## Running the test suite

### Dependencies

- Python 3
- `pip install -r requirements.txt`
- Docker (supports remote docker hosts via the `DOCKER_HOST` environment variable)

### Setup

1. Put any environment variables specific for your machine in a `.env` file, which will be loaded by `pytest` before it runs the test suite.

    A few environment variables to consider:
    - [docker environment variables][env-vars-docker], e.g. `DOCKER_HOST` if you want to run the test suite examples on a different Docker host, or use other Docker settings
    - [`PYTEST_XDIST_AUTO_NUM_WORKERS`][env-vars-pytest-xdist] can be set to the number of worker processes to run the tests in if `pytest-xdist`'s `auto` setting is not what you want.
    - [`pytest`][env-vars-pytest] environment variables

2. Make sure you Docker host is running

### Run the test suite

Run `pytest` from the command line. If you are using VSCode you'll see the tests in the Testing panel.

#### Running individual tests

Use pytest's `-k` to narrow down wich tests to run. Examples:

| command                            | narrows down to                       |
| ---------------------------------- | ------------------------------------- |
| `pytest -k ruby`                   | Ruby tests                            |
| `pytest -k 'ruby and null_char'`   | Only Ruby's null_char test            |
| `pytest -k 'ruby and json'`        | Ruby's JSON tests                     |
| `pytest -k java`                   | java **and** **java**script tests     |
| `pytest -k '[java]'`               | only java tests, not javascript tests |
| `pytest -k '[java] and null_char'` | only java tests, not javascript tests |

#### Running locally

Mark a test with `@pytest.mark.local` if you want it to run the tested script locally instead of in docker. E.g.

```python
# Will run in docker as
#   docker run -i python-rosetta /bin/sh -c 'python encode.py "Hello World!"'
def test_encode(self, script):
    script.run("encode", '"Hello, world!"')
    assert script.output == 'SGVsbG8sIHdvcmxkIQ==\n'

# Will run on your machine as:
#   /bin/sh -c 'python encode.py "Hello World!"'
@pytest.mark.local
def test_encode(self, script):
    script.run("encode", '"Hello, world!"')
    assert script.output == 'SGVsbG8sIHdvcmxkIQ==\n'
```

Alternatively, you can set the `TEST_LOCAL` environment variable to `true` or `1` to run all tests locally without having to mark them with `@pytest.mark.local`.

E.g. run all Swift tests locally:

```bash
TEST_LOCAL=1 pytest -k swift
```


[env-vars-docker]: https://docs.docker.com/engine/reference/commandline/cli/#environment-variables
[env-vars-pytest-xdist]: https://pytest-xdist.readthedocs.io/en/stable/distribution.html
[env-vars-pytest]: https://docs.pytest.org/en/7.4.x/reference/reference.html#environment-variables

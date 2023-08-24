# I/O ergonomics of popular languages

Working examples of how popular languages handle basic I/O and common serialization formats.

The examples are validated via a test suite that runs the examples in Docker and verifies expected behavior.

This project is not currently meant to be exhaustive in terms of languages, operating systems and I/O operations. The languages and I/O operations, etc are prioritized to support a commercial devtool product currently in stealth mode. That being said, contributions are very welcome.

The name `rosetta-io` is an hommage to [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code) but is not affiliated.

## Languages covered

| Language            | Status      |
| ------------------- | ----------- |
| Python 3            | WIP         |
| Javascript, Node.js | Not started |
| R                   | Not started |
| Ruby                | Not started |
| PHP                 | Not started |
| …                   |             |

## Running the test suite

### Dependencies

- Python 3
- `pip install -r requirements.txt`
- Docker (supports remote docker hosts via the `DOCKER_HOST` environment variable)

### Setup

1. Put any environment variables you need in a `.env` file, which will be loaded by  `pytest` before it runs the tests.

    E.g. if you want to run the test suite examples on a different Docker host, set the `DOCKER_HOST` env variable.

3. Make sure you Docker host is running

### Run the test suite

Run `pytest` from the command line. If you are using VSCode you'll see the tests in the Testing panel.

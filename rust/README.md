# Rust

## setup

To run locally, you'll need to first install the `cargo-script` tool:

```bash
cd ./rust # must be in this directory
cargo install cargo-script
```
## Fix `ERROR:cargo_script::util: deferred function failed: No such file or directory` error

Do this, which should fix the error:
```bash
cd ./rust # must be in this directory
cargo-script --clear-cache

cd ..
TEST_LOCAL=1 pytest -k 'rust' -n0 # run all tests, but not in parallel, populating the cache correctly
```

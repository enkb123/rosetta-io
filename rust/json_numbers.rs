//cargo-deps: json="0.12.4"

// Script takes string arguments and outputs a JSON array of numbers representing
// the length of each argument
use json::JsonValue;
use std::env;

extern crate json;

fn main() {
    let args = env::args().skip(1);

    let json_array: JsonValue = args
        .map(|arg| arg.len().into())
        .collect::<Vec<JsonValue>>()
        .into();

    println!("{}", json_array.to_string());
}

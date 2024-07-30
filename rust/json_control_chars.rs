//cargo-deps: json="0.12.4"

//Script takes control characters and outputs valid JSON
use json::JsonValue;
use std::env;

extern crate json;

fn main() {
    let args: Vec<String> = env::args().collect();

    let test_string = &args[1];

    let json_value = JsonValue::String(test_string.clone());

    println!("{}", json_value.dump());
}

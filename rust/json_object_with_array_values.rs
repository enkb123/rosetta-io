//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;

extern crate json;

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();

    let mut json_object = JsonValue::new_object();

    for arg in args {
        let letters_array: JsonValue = arg
            .to_uppercase()
            .chars()
            .map(|c| c.to_string().into())
            .collect::<Vec<JsonValue>>()
            .into();

        json_object[arg] = letters_array;
    }

    println!("{}", json_object.dump());
}

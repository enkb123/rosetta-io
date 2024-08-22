//cargo-deps: json="0.12.4"

// Script outputs arrays of objects as JSON
use json::JsonValue;
use std::env;

extern crate json;
fn main() {
    let args: Vec<String> = env::args().skip(1).collect();

    let json_array = JsonValue::Array(
        args.into_iter()
            .map(|string| {
                let mut obj = JsonValue::new_object();
                obj[string.to_uppercase()] = JsonValue::Number(string.len().into());
                obj
            })
            .collect(),
    );

    println!("{}", json_array.dump());
}

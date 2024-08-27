//cargo-deps: json="0.12.4"

// Script outputs arrays of objects as JSON
use json::JsonValue;
use std::env;
use json::object;

extern crate json;
fn main() {
    let args = env::args().skip(1);
    let json_array = JsonValue::Array(
        args.into_iter()
            .map(|string| {
                object! {
                    string.to_uppercase().as_str() => string.len()
                }
            })
            .collect(),
    );

    println!("{}", json_array.dump());
}

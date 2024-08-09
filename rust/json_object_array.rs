//cargo-deps: json="0.12.4"

// Script outputs arrays of objects as JSON
use std::env;
use json::JsonValue;
use json::object;

extern crate json;
fn main() {
    let args: Vec<String> = env::args().skip(1).collect();

    let mut json_array = JsonValue::new_array();

    for arg in args {
        let key = arg.to_uppercase();
        let value = arg.len();

        let json_object = object! {
            key.as_str() => value as usize
          };

        json_array.push(json_object).unwrap();
    }

    println!("{}", json_array);
}

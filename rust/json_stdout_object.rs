//cargo-deps: json="0.12.4"

// Script reads string args and transforms into dict

use std::env;
use json::JsonValue;

extern crate json;
fn main() {
    let args: Vec<String> = env::args().collect();

    let mut json_object = JsonValue::new_object();

    for arg in &args[1..] {
        json_object[arg] = JsonValue::Number((arg.len() as i64).into());
    }

    println!("{}", json_object.dump());
}

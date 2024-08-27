//cargo-deps: json="0.12.4"

// Script reads string args and transforms into dict

use json::JsonValue;
use std::env;

extern crate json;
fn main() {
    let args = env::args().skip(1);
    let mut json_object = JsonValue::new_object();

    for arg in args {
        json_object[arg] = arg.len().into();
    }

    println!("{}", json_object.dump());
}

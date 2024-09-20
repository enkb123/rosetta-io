//cargo-deps: json="0.12.4"

extern crate json;

use json::{JsonValue, object};

fn main() {
    let first_json_object = object! {
        "true" => true,
        "false" => false,
        "zero" => 0,
        "int" => 42,
        "float" => 3.14,
        "null" => JsonValue::Null,
        "empty string" => "",
        "a string with non-ascii characters" => "hello \n \0 \u{0001} world 🥸"
    };

    let second_json_object = object! {
        "array of strings" => JsonValue::Array(vec![
            "abc".into(),
            "def".into(),
            "ghi".into(),
            "jkl".into()
        ]),
        "array of numbers" => JsonValue::Array(vec![
            13.into(),
            42.into(),
            9000.into(),
            (-7).into()
        ]),
        "array of nothing" => JsonValue::Array(vec![]),
        "array of mixed" => JsonValue::Array(vec![
            13.into(),
            "def".into(),
            JsonValue::Null,
            false.into(),
            JsonValue::Array(vec!["a".into()]),
            object! { "o" => 1 }
        ]),
        "array of objects" => JsonValue::Array(vec![
            object! { "name" => "Bob Barker", "age" => 84 },
            object! { "address1" => "123 Main St", "address2" => "Apt 1" }
        ]),
        "array of arrays" => JsonValue::Array(vec![
            JsonValue::Array(vec!["a".into(), "b".into(), "c".into()]),
            JsonValue::Array(vec!["d".into(), "e".into(), "f".into()])
        ])
    };

    let third_json_object = object! {
        "objects" => object! {
            "nested" => object! {
                "objects" => object! {
                    "are" => "supported"
                }
            }
        }
    };

    println!("{}", first_json_object.dump());
    println!("{}", second_json_object.dump());
    println!("{}", third_json_object.dump());
}

// cargo-deps: json="0.12.4"

extern crate json;

use json::{array, object, JsonValue};

fn main() {
    let first_json_object = object! {
        "true" => true,
        "false" => false,
        "zero" => 0,
        "int" => 42,
        "float" => 3.14,
        "null" => JsonValue::Null,
        "empty string" => "",
        "a string with non-ascii characters" => "hello \n \u{0001} world 🥸"
    };

    let second_json_object = object! {
        "array of strings" => array!["abc", "def", "ghi", "jkl"],
        "array of numbers" => array![13, 42, 9000, -7],
        "array of nothing" => array![],
        "array of mixed" => array![13, "def", JsonValue::Null, false, array!["a"], object! { "o" => 1 }],
        "array of objects" => array![
            object! { "name" => "Bob Barker", "age" => 84 },
            object! { "address1" => "123 Main St", "address2" => "Apt 1" }
        ],
        "array of arrays" => array![
            array!["a", "b", "c"],
            array!["d", "e", "f"]
        ]
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

    println!("{}", first_json_object);
    println!("{}", second_json_object);
    println!("{}", third_json_object);
}

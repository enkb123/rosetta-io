// cargo-deps: json="0.12.4"

extern crate json;

fn main() {
    println!("{}", json::stringify("Hello World \0"));
}

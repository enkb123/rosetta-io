use std::fs::write;

fn main() {
    write("output.pipe", "Hello World!").unwrap();
}

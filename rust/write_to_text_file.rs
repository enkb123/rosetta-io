use std::fs::write;

fn main() {
    write("output.txt", "Hello World!").unwrap();
}

use std::env;
use std::fs::write;

fn main() {
   let out_file = "output.txt";
    let text = "Hello World!";

    write(out_file, text).unwrap();
}

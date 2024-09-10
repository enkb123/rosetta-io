use std::env;
use std::fs::write;

fn main() {
    let args: Vec<String> = env::args().collect();

    let out_file = &args[1];
    let text = &args[2].to_uppercase();

    write(out_file, text).unwrap();
}

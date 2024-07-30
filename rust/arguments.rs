// Script to read an argument and print as lowercase in stdout

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let user = &args[1];

    println!("{}", user.to_lowercase());
}

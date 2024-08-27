// Script to read an argument and print as lowercase in stdout

use std::env;

fn main() {
    let user = env::args().nth(1).expect("Expected one argument");
    println!("{}", user.to_lowercase());
}

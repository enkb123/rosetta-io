use std::env;

fn main() {
    let user = env::args().nth(1).expect("Expected one argument");
    println!("{}", user.to_lowercase());
}

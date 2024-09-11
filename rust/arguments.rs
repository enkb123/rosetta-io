use std::env;

fn main() {
    let user = env::args().nth(1).unwrap();
    println!("{}", user.to_lowercase());
}

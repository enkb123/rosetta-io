use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    println!("1st argument: {}", args[1]);
    println!("2nd argument: {}", args[2]);
}

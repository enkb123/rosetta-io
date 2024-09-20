use std::io::{self, BufRead};

fn main() {
    for maybe_line in io::stdin().lock().lines() {
        let line = maybe_line.unwrap().trim().to_string();
        if line.is_empty() {
            break;
        }
        println!("received {}", line);
    }
}

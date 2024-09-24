use std::io::{self, stdin, BufRead};

fn main() {
    for line in stdin().lock().lines() {
        println!("line: {}", line.unwrap());
    }
}

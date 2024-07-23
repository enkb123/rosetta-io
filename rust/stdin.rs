// Test script to get input, transform, and write to stdout
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let lines = stdin.lock().lines().map(|line| line.unwrap());

    for (counter, line) in lines.enumerate() {
        let line = line.trim();
        if line.is_empty() {
            break;
        }
        println!("{} {}", counter + 1, line.to_uppercase());
    }
}

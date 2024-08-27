// Test script to get input, transform, and write to stdout
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    for (counter, line) in stdin.lock().lines().enumerate() {
        let line = line.unwrap().trim().to_string();
        if line.is_empty() {
            break;
        }
        println!("{} {}", counter + 1, line.to_uppercase());
    }
}

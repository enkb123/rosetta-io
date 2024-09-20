use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    for line in stdin.lock().lines(){
        let line = line.unwrap().trim().to_string();
        if line.is_empty() {
            break;
        }
        println!("line: {}", line);
    }
}

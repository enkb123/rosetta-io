//Script to write text to a new file
//Run script as `cargo write_file.rs <output_file>.txt 'some text'`

use std::env;
use std::fs::write;

fn main() {
    let args: Vec<String> = env::args().collect();

    let out_file = &args[1];
    let text = &args[2].to_uppercase();

    let _ = write(out_file, text);
}

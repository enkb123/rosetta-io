/*Script to write text to a new file.
Run script as `swift write_file.py <output_file>.swift "some text"`
*/

import Foundation

guard CommandLine.arguments.count == 3 else {
    print("Usage: swift script.swift <outfile> <text>")
    exit(1)
}

let outfile = CommandLine.arguments[1]
let text = CommandLine.arguments[2]

// atomically must be false when writing to named pipe
try text.uppercased().write(toFile: outfile, atomically: false, encoding: .utf8)

/*Script to write text to a new file.
Run script as `swift write_file.py <output_file>.swift "some text"`
*/

import Foundation

guard CommandLine.arguments.count > 2 else {
    print("Usage: swift script.swift <outfile> <text>")
    exit(1)
}

let outfile = CommandLine.arguments[1]
let text = CommandLine.arguments[2]

do {
    try text.uppercased().write(toFile: outfile, atomically: true, encoding: .utf8)
} catch {
    print("Error writing to \(outfile):", error.localizedDescription)
    exit(1)
}

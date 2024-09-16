import Foundation

guard CommandLine.arguments.count == 3 else {
    print("Usage: swift script.swift <outfile> <text>")
    exit(1)
}

let outfile = CommandLine.arguments[1]
let text = CommandLine.arguments[2]

try text.uppercased().write(toFile: outfile, atomically: false, encoding: .utf8)

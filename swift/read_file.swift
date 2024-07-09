//Read a file (file path given as a command line argument) and write to stdout


import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <file_path>")
    exit(1)
}

let fileURL = URL(fileURLWithPath: CommandLine.arguments[1])
let fileContents = try String(contentsOf: fileURL)
var i = 1
fileContents.enumerateLines { line, _ in
    print("\(i) \(line.uppercased())")
    i += 1
}



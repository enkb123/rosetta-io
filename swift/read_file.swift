import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <file_path>")
    exit(1)
}

let fileContents = try String(contentsOfFile: CommandLine.arguments[1])
var i = 1
fileContents.enumerateLines { line, _ in
    print("\(i) \(line.uppercased())")
    i += 1
}

import Foundation

guard CommandLine.arguments.count == 2 else {
    print("Usage: swift JsonControlChars.swift <test_string>")
    exit(1)
}

let testString = CommandLine.arguments[1]

let jsonData = try JSONEncoder().encode(testString)
print(String(data: jsonData, encoding: .utf8)!)

//Script takes control characters and outputs valid JSON
import Foundation

guard CommandLine.arguments.count == 2 else {
    print("Usage: swift JsonControlChars.swift <test_string>")
    exit(1)
}

let testString = CommandLine.arguments[1]

let jsonData = try JSONEncoder().encode(testString)

if let jsonString = String(data: jsonData, encoding: .utf8) {
    print(jsonString)
}


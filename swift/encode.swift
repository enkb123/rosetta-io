import Foundation

guard CommandLine.arguments.count == 2 else {
    print("Usage: swift script.swift <test_string>")
    exit(1)
}

let data = CommandLine.arguments[1].data(using: .utf8)!
print(data.base64EncodedString())

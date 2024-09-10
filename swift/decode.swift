#!/usr/bin/swift

import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: \(CommandLine.arguments[0]) <encoded_string>")
    exit(1)
}

let encodedString = CommandLine.arguments[1]
let data = Data(base64Encoded: encodedString)
print(String(data: data!, encoding: .utf8)!)

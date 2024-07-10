//Script takes args and turns into JSON array

import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = Array(CommandLine.arguments.dropFirst())
let jsonData = try JSONSerialization.data(withJSONObject: myStrings)
print(String(data: jsonData, encoding: .utf8) as! String)


//Script reads string args and transforms into python dict
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = CommandLine.arguments.dropFirst()
let stringLengthDict = Dictionary(uniqueKeysWithValues: myStrings.map { ($0, $0.count) })

let jsonData = try JSONSerialization.data(withJSONObject: stringLengthDict)
print(String(data: jsonData, encoding: .utf8)!)

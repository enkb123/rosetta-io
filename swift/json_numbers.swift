//Script takes args and outputs a list of lengths
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = Array(CommandLine.arguments.dropFirst())

let stringLengths = myStrings.map { $0.count }

let jsonData = try JSONSerialization.data(withJSONObject: stringLengths)
print(String(data: jsonData, encoding: .utf8) as! String)




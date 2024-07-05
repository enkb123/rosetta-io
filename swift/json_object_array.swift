//Script writes an array of objects to stdout
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let args = Array(CommandLine.arguments.dropFirst())

let myArray = args.map { arg -> [String: Any] in
    return [arg.uppercased(): arg.count]
}

let jsonData = try JSONSerialization.data(withJSONObject: myArray, options: .prettyPrinted)

if let jsonString = String(data: jsonData, encoding: .utf8) {
    print(jsonString)
}



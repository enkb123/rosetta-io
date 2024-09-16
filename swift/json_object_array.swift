import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let args = CommandLine.arguments.dropFirst()

let myArray = args.map { [$0.uppercased(): $0.count] }

let jsonData = try JSONSerialization.data(withJSONObject: myArray)
print(String(data: jsonData, encoding: .utf8)!)

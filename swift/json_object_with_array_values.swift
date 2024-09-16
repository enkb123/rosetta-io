import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = CommandLine.arguments.dropFirst()

let stringLettersDict = Dictionary(uniqueKeysWithValues: myStrings.map {
    ($0, $0.map { String($0).uppercased() })
})

let jsonData = try JSONSerialization.data(withJSONObject: stringLettersDict)
print(String(data: jsonData, encoding: .utf8)!)

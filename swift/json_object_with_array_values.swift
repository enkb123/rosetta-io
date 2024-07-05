//Script takes args and transforms into python dict with arrays as dict values
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = Array(CommandLine.arguments.dropFirst())

let stringLettersDict = Dictionary(uniqueKeysWithValues: myStrings.map {
    ($0, $0.map { String($0).uppercased() })
})

let jsonData = try JSONSerialization.data(withJSONObject: stringLettersDict, options: .prettyPrinted)

if let jsonString = String(data: jsonData, encoding: .utf8) {
    print(jsonString)
}



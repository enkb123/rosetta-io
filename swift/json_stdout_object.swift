import Foundation

let myStrings = CommandLine.arguments.dropFirst()
let stringLengthDict = Dictionary(uniqueKeysWithValues: myStrings.map { ($0, $0.count) })

let jsonData = try JSONSerialization.data(withJSONObject: stringLengthDict)
print(String(data: jsonData, encoding: .utf8)!)

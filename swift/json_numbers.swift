import Foundation

let myStrings = CommandLine.arguments.dropFirst()

let stringLengths = myStrings.map { $0.count }

let jsonData = try JSONSerialization.data(withJSONObject: stringLengths)
print(String(data: jsonData, encoding: .utf8)!)

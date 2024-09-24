import Foundation

let testString = CommandLine.arguments[1]

let jsonData = try JSONEncoder().encode(testString)
print(String(data: jsonData, encoding: .utf8)!)

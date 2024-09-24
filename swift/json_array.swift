import Foundation

let myStrings = Array(CommandLine.arguments.dropFirst())
let jsonData = try JSONSerialization.data(withJSONObject: myStrings)
print(String(data: jsonData, encoding: .utf8)!)

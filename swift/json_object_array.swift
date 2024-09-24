import Foundation

let args = CommandLine.arguments.dropFirst()

let myArray = args.map { [$0.uppercased(): $0.count] }

let jsonData = try JSONSerialization.data(withJSONObject: myArray)
print(String(data: jsonData, encoding: .utf8)!)

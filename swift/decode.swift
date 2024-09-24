import Foundation

let encodedString = CommandLine.arguments[1]
let data = Data(base64Encoded: encodedString)
print(String(data: data!, encoding: .utf8)!)

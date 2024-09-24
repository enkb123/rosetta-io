import Foundation

let data = CommandLine.arguments[1].data(using: .utf8)!
print(data.base64EncodedString())

import Foundation

let str = "Hello World \0"

let data = try JSONEncoder().encode(str)
print(String(data: data, encoding: .utf8)!)

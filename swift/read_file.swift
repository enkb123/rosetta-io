import Foundation

let filePath = "./my-text-file.txt"

let content = try String(contentsOfFile: filePath, encoding: .utf8)
let lines = content.components(separatedBy: .newlines)
for line in lines {
    if !line.isEmpty {
        print("line: \(line)")
    }
}

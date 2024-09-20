import Foundation

let filePath = "./my-text-file.txt"
let fileURL = URL(fileURLWithPath: filePath)

let content = try String(contentsOf: fileURL, encoding: .utf8)
let lines = content.components(separatedBy: .newlines)
for line in lines {
    if !line.isEmpty {
        print("line: \(line)")
    }
}

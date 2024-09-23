import Foundation

let outfile = "output.txt"
let text = "Hello World!"

try text.write(toFile: outfile, atomically: false, encoding: .utf8)

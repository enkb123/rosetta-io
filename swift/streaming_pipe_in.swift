import Foundation

/*
  Turn off output buffering for stdout
*/
#if os(macOS) || os(iOS)
  import Darwin
#elseif os(Linux)
  import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

/*
  Like readLine(), but for reading from a file/pipe
*/
func readFileLine(file: UnsafeMutablePointer<FILE>) -> String? {
  var line: UnsafeMutablePointer<CChar>? = nil
  var n = 0
  defer { free(line) }
  return getline(&line, &n, file) > 0 ? String(cString: line!) : nil
}

let pipeIn = fopen("input.pipe", "r")!

while let line = readFileLine(file: pipeIn) {
  print(line.uppercased(), terminator: "")
}

fclose(pipeIn)

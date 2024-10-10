import Foundation

/*
  Like readLine(), but for reading from a file/pipe
*/
func readFileLine(file: UnsafeMutablePointer<FILE>) -> String? {
  var line: UnsafeMutablePointer<CChar>? = nil
  var n = 0
  defer { free(line) }
  return getline(&line, &n, file) > 0 ? String(cString: line!) : nil
}

let pipeIn = fopen("streaming-in.pipe", "r")!
let pipeOutHandle = open("streaming-out.pipe", O_WRONLY)

while let line = readFileLine(file: pipeIn) {
  let outputLine = "received \(line)"
  write(pipeOutHandle, outputLine, outputLine.utf8.count)
}

fclose(pipeIn)

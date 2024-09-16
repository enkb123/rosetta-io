import Foundation

#if os(macOS) || os(iOS)
  import Darwin
#elseif os(Linux)
  import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

let arguments = CommandLine.arguments
let pipe_in = arguments[1]

let pipe_out = arguments[2]
let fileDescriptor = open(pipe_out, O_WRONLY)

public class FileLines: Sequence, IteratorProtocol {
  private let file: UnsafeMutablePointer<FILE>

  init?(path: String) {
    guard let file = fopen(path, "r") else { return nil }
    self.file = file
  }

  public func next() -> String? {
    var line: UnsafeMutablePointer<CChar>? = nil
    var linecap: Int = 0
    defer { free(line) }
    return getline(&line, &linecap, file) > 0 ? String(cString: line!) : nil
  }

  deinit {
    fclose(file)
  }

  public func makeIterator() -> FileLines {
    return self
  }
}

// in new versions of Swift, this can be replaced with `if let lines = FileHandle(forReadingAtPath: pipe_in).bytes.lines`
if let lines = FileLines(path: pipe_in) {
  for line in lines {
    write(fileDescriptor, line.uppercased(), line.uppercased().utf8.count)
  }
} else {
  print("Error reading from pipe: Could not open file at path \(pipe_in)")
}

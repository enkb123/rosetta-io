#if os(macOS) || os(iOS)
import Darwin
#elseif os(Linux)
import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

import Foundation

let arguments = CommandLine.arguments

let pipe_in = arguments[1]

let fileHandle = FileHandle(forReadingAtPath: pipe_in)!

for try await line in fileHandle.bytes.lines {
    print(line.uppercased())
}

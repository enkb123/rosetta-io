#if os(macOS) || os(iOS)
import Darwin
#elseif os(Linux)
import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

import Foundation

let arguments = CommandLine.arguments

let pipe_in = arguments[1]

guard let inputStream = InputStream(fileAtPath: pipe_in) else {
    fatalError("Cannot open input stream")
}

inputStream.open()

let bufferSize = 1024
let buffer = UnsafeMutablePointer<UInt8>.allocate(capacity: bufferSize)

while true {
    let bytesRead = inputStream.read(buffer, maxLength: bufferSize)

    let inputString = String(bytesNoCopy: buffer, length: bytesRead, encoding: .utf8, freeWhenDone: false)

    let uppercaseString = inputString?.uppercased() ?? ""

    print(uppercaseString, terminator: "")

}

inputStream.close()
buffer.deallocate()

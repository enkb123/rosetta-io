// Script reads streaming input text and then prints capitalized string to stdout

// Turn off buffering for stdout
#if os(macOS) || os(iOS)
import Darwin
#elseif os(Linux)
import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

import Foundation

while let line = readLine(), !line.isEmpty {
    print(line.uppercased())
}






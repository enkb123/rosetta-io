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

while let line = readLine() {
  print("received \(line)")
}

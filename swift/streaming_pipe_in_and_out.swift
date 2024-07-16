//Script reads text from a named pipe and writes it another named pipe, capitalized
import Foundation

    let arguments = CommandLine.arguments

    let pipe_in = arguments[1]
    let pipe_out = arguments[2]

    let inputStream = InputStream(fileAtPath: pipe_in)
    inputStream?.open()

    let outputStream = OutputStream(toFileAtPath: pipe_out, append: false)
    outputStream?.open()

    let bufferSize = 1024
    let buffer = UnsafeMutablePointer<UInt8>.allocate(capacity: bufferSize)

    while inputStream!.hasBytesAvailable {
        let bytesRead = inputStream!.read(buffer, maxLength: bufferSize)
        let inputString = String(bytesNoCopy: buffer, length: bytesRead, encoding: .utf8, freeWhenDone: false)
        if let uppercaseString = inputString?.uppercased() {
            outputStream!.write(uppercaseString, maxLength: uppercaseString.utf8.count)
        }
    }

    inputStream?.close()
    outputStream?.close()

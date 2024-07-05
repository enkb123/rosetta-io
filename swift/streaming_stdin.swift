//everything I try either only reads the first line or gets stuck in an endless loop
import Foundation

// Setup standard input
let input = FileHandle.standardInput

// Create a DispatchQueue for handling input
let queue = DispatchQueue.global()

// Read data asynchronously
input.readabilityHandler = { handle in
    // Read available data
    let data = handle.availableData

    // Convert data to string
    if let inputString = String(data: data, encoding: .utf8) {
        // Split input into lines
        let lines = inputString.components(separatedBy: .newlines)

        // Process each line
        for line in lines {
            // Print each line in uppercase
            print(line.uppercased())
        }
    }
}

// Keep the program running until interrupted
RunLoop.current.run()

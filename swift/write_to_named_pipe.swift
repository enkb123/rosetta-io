import Foundation

let pipePath = "output.pipe"

if !FileManager.default.fileExists(atPath: pipePath) {
    mkfifo(pipePath, 0o644)
}

if let pipe = fopen(pipePath, "w") {
    fputs("Hello World!\n", pipe)
    fclose(pipe)
}

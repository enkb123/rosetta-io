#!/usr/bin/swift

import Foundation

let args = CommandLine.arguments

guard args.count > 1 else {
    print("Usage: \(args[0]) <argument>");
    exit(1)
}

print(args[1].lowercased())

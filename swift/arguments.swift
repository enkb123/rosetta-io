import Foundation

let args = CommandLine.arguments

guard args.count > 1 else {
    print("Usage: \(args[0]) <argument>");
    exit(1)
}

print("1st argument: \(args[1])")
print("2nd argument: \(args[2])")

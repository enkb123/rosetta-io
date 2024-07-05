#!/usr/bin/swift
//Script to encode a string as Base64
import Foundation

guard CommandLine.arguments.count == 2 else {
    print("Usage: swift script.swift <test_string>")
    exit(1)
}

let testString = CommandLine.arguments[1]

guard let data = testString.data(using: .utf8) else {
    print("Error encoding string to data")
    exit(1)
}

print(data.base64EncodedString())

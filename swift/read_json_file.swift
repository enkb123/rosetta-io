//Read JSON file, transform and print to stdout
import Foundation

guard let jsonFile = CommandLine.arguments.dropFirst().first else {
    print("Usage: swift script.swift <json_file>")
    exit(1)
}

do {
    let fileURL = URL(fileURLWithPath: jsonFile)
    let jsonData = try Data(contentsOf: fileURL)
    let people = try JSONSerialization.jsonObject(with: jsonData) as? [[String: Any]] ?? []

    for (index, person) in people.enumerated() {
        if let age = person["age"] as? Int, let firstName = person["first_name"] as? String {
            print("Hello, \(age) year old \(firstName)")
        }
    }
} catch {
    print("Error reading or parsing JSON file:", error.localizedDescription)
    exit(1)
}

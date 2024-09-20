import Foundation

let jsonFile = "people.json"

let fileURL = URL(fileURLWithPath: jsonFile)
let jsonData = try Data(contentsOf: fileURL)
let people = try JSONSerialization.jsonObject(with: jsonData) as! [[String: Any]]

for (_, person) in people.enumerated() {
    let age = person["age"] as! Int
    let firstName = person["first_name"] as! String

    print("Hello, \(age) year old \(firstName)")
}

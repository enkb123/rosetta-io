import Foundation

let firstJsonObject: [String: Any] = [
    "true": true,
    "false": false,
    "zero": 0,
    "int": 42,
    "float": 3.14,
    "null": NSNull(),
    "empty string": "",
    "a string with non-ascii characters": "hello \n \0 \u{0001} world 🥸"
]

let secondJsonObject: [String: Any] = [
    "array of strings": ["abc", "def", "ghi", "jkl"],
    "array of numbers": [13, 42, 9000, -7],
    "array of nothing": [],
    "array of mixed": [13, "def", NSNull(), false, ["a"], ["o": 1]],
    "array of objects": [
        ["name": "Bob Barker", "age": 84],
        ["address1": "123 Main St", "address2": "Apt 1"]
    ],
    "array of arrays": [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
]

let thirdJsonObject: [String: Any] = [
    "objects": [
        "nested": [
            "objects": [
                "are": "supported"
            ]
        ]
    ]
]

func jsonString(from dictionary: [String: Any]) -> String {
    let jsonData = try! JSONSerialization.data(withJSONObject: dictionary, options: [])
    return String(data: jsonData, encoding: .utf8)!
}

print(jsonString(from: firstJsonObject))
print(jsonString(from: secondJsonObject))
print(jsonString(from: thirdJsonObject))

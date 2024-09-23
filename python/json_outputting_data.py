import json

first_json_object = {
    "true": True,
    "false": False,
    "zero": 0,
    "int": 42,
    "float": 3.14,
    "null": None,
    "empty string": "",
    "a string with non-ascii characters": "hello \n \0 \x01 world 🥸"
}

second_json_object = {
    "array of strings": ["abc", "def", "ghi", "jkl"],
    "array of numbers": [13, 42, 9000, -7],
    "array of nothing": [],
    "array of mixed": [13, "def", None, False, ["a"], {"o": 1}],
    "array of objects": [
        {"name": "Bob Barker", "age": 84},
        {"address1": "123 Main St", "address2": "Apt 1"}
    ],
    "array of arrays": [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
}

third_json_object = {
    "objects": {
        "nested": {
            "objects": {
                "are": "supported"
            }
        }
    }
}

print(json.dumps(first_json_object))
print(json.dumps(second_json_object))
print(json.dumps(third_json_object))

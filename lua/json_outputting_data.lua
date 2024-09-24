local json = require("dkjson")

local firstJsonObject = {
    ["true"] = true,
    ["false"] = false,
    ["zero"] = 0,
    ["int"] = 42,
    ["float"] = 3.14,
    ["null"] = json.null,
    ["empty string"] = "",
    ["a string with non-ascii characters"] = "hello \n \0 \u{0001} world 🥸"
}

local secondJsonObject = {
    ["array of strings"] = {"abc", "def", "ghi", "jkl"},
    ["array of numbers"] = {13, 42, 9000, -7},
    ["array of nothing"] = {},
    ["array of mixed"] = {13, "def", json.null, false, {"a"}, {["o"] = 1}},
    ["array of objects"] = {
        {["name"] = "Bob Barker", ["age"] = 84},
        {["address1"] = "123 Main St", ["address2"] = "Apt 1"}
    },
    ["array of arrays"] = {
        {"a", "b", "c"},
        {"d", "e", "f"}
    }
}

local thirdJsonObject = {
    ["objects"] = {
        ["nested"] = {
            ["objects"] = {
                ["are"] = "supported"
            }
        }
    }
}

print(json.encode(firstJsonObject))
print(json.encode(secondJsonObject))
print(json.encode(thirdJsonObject))

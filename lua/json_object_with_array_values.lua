-- Lua script to transform string arguments into a Lua table of arrays and output as JSON

local cjson = require("dkjson")

local string_letters_dict = {}

for i = 1, #arg do
    local string = arg[i]
    local letters = {}

    for letter in string:gmatch(".") do
        table.insert(letters, letter:upper())
    end
    string_letters_dict[string] = letters
end

print(cjson.encode(string_letters_dict))

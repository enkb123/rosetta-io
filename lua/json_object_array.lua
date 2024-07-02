-- Lua script to transform string arguments into an array of dictionaries and output as JSON

local cjson = require("cjson")

local my_array = {}

for i = 1, #arg do
    local string = arg[i]
    local dict = {}
    dict[string:upper()] = string:len()
    table.insert(my_array, dict)
end

print(cjson.encode(my_array))

-- Lua script to transform string arguments into an array of dictionaries and output as JSON

local cjson = require("dkjson")

local my_array = {}

for i = 1, #arg do
    local string = arg[i]
    table.insert(my_array, {
        [arg[i]:upper()] = arg[i]:len()
    })
end

print(cjson.encode(my_array))

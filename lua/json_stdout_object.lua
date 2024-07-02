-- Lua script to transform string arguments into a Lua table and output as JSON

local cjson = require("cjson")

local dict = {}

for i = 1, #arg do
    dict[arg[i]] = string.len(arg[i])
end

print(cjson.encode(dict))

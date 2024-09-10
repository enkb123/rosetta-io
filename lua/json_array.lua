-- Lua script to convert command-line arguments to JSON array

local cjson = require("dkjson")

local args = {}
for i = 1, #arg do
    table.insert(args, arg[i])
end

print(cjson.encode(args))

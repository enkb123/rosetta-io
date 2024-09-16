local cjson = require("dkjson")

local lengths = {}
for i = 1, #arg do
    table.insert(lengths, string.len(arg[i]))
end

print(cjson.encode(lengths))

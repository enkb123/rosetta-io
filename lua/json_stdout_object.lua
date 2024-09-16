local cjson = require("dkjson")

local dict = {}

for i = 1, #arg do
    dict[arg[i]] = arg[i]:len()
end

print(cjson.encode(dict))

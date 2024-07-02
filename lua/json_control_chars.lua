-- Lua script to output valid JSON from a string argument

local cjson = require("cjson")

print(cjson.encode(arg[1]))

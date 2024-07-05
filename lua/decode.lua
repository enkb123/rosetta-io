-- Lua script to decode Base64 encoded string from command-line argument

local base64 = require("base64")
print(base64.decode(arg[1]))


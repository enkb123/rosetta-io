-- Lua script to read input, transform to uppercase, and print with line numbers
local file_path = arg[1]
local fh = io.open(arg[1], "r")
local i = 1

for line in fh:lines() do
    print(i .. " " .. line:upper())
    i = i + 1
end


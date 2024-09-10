local file_path = arg[1]
local fh = io.open(file_path, "r")
local i = 1

for line in fh:lines() do
    print(i .. " " .. line:upper())
    i = i + 1
end

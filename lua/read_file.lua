local filePath = "./my-text-file.txt"

local file = io.open(filePath, "r")

for line in file:lines() do
    print("line: " .. line)
end
file:close()

local filename = "output.txt"
local text = "Hello World!"

local file = io.open(filename, "w")

if file then
    file:write(text)
    file:close()
end

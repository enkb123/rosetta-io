-- Script reads text from a named pipe and writes it to stdout, capitalized
local pipe_in = arg[1]

local input_file = assert(io.open(pipe_in, "r"), "Failed to open input pipe: " .. pipe_in)

while true do
    local line = input_file:read("*l")
    if not line then
        break
    end
    io.write(line:upper() .. "\n")
    io.flush()
end

input_file:close()

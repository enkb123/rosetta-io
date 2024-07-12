-- Script reads text from a named pipe and writes it another named pipe, capitalized
local pipe_in = arg[1]
local pipe_out = arg[2]

local input_file = io.open(pipe_in, "r")

local output_file = io.open(pipe_out, "w")

while true do
    local line = input_file:read("*l")
    if not line then
        break
    end
    output_file:write(line:upper(), "\n")
    output_file:flush()
end

input_file:close()
output_file:close()

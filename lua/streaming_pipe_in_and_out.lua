local pipe_in = arg[1]
local pipe_out = arg[2]

local input_file = io.open(pipe_in, "r")

local output_file = io.open(pipe_out, "w")

for line in input_file:lines() do
    output_file:write(line:upper(), "\n")
    output_file:flush()
end

input_file:close()
output_file:close()

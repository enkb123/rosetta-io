local pipe_in = "input.pipe"

local input_file = assert(io.open(pipe_in, "r"), "Failed to open input pipe: " .. pipe_in)

for line in input_file:lines() do
    io.write(line:upper() .. "\n")
    io.flush()
end

input_file:close()

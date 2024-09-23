local input_file = "streaming-in.pipe"
local output_file = "streaming-out.pipe"

local output = io.open(output_file, "w")

local input = io.open(input_file, "r")

for line in input:lines() do
    output:write("received " .. line .. "\n")
    output:flush()
end

input:close()
output:close()

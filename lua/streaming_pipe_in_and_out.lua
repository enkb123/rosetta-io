local output = io.open("streaming-out.pipe", "w")
local input = io.open("streaming-in.pipe", "r")

for line in input:lines() do
    output:write("received " .. line .. "\n")
    output:flush()
end

input:close()
output:close()

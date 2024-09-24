local input_file = io.open("input.pipe", "r")

for line in input_file:lines() do
    io.write(line:upper() .. "\n")
    io.flush()
end

input_file:close()

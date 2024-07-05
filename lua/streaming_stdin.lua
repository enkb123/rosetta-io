-- Lua script to read streaming input and print capitalized string to stdout

-- Read all input lines and capitalize each line, then print
for line in io.lines() do
    print(line:upper())
end

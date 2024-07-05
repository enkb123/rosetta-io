-- Lua script to read input, transform to uppercase, and print with line numbers
local i = 1

-- Read from stdin until EOF
for user_input in io.lines() do
    -- Transform input to uppercase and prepend with line number
    print(i .. " " .. user_input:upper())
    i = i + 1
end



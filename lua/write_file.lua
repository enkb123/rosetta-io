-- Lua script to write text to a new file
-- Run script as `lua write_file.lua <output_file>.txt 'some text'`

local outfile = arg[1]
local text = arg[2]

local fh = io.open(outfile, "w")

fh:write(text:upper())

fh:close()

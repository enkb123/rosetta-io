local outfile = arg[1]
local text = arg[2]

local fh = io.open(outfile, "w")

fh:write(text:upper())

fh:close()

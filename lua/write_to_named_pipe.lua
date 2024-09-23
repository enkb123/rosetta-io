local pipePath = "output.pipe"

os.execute("mkfifo " .. pipePath)

local pipe = io.open(pipePath, "w")
pipe:write("Hello World!\n")
pipe:close()

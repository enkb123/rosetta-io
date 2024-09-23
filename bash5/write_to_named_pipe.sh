pipe_out="output.pipe"

mkfifo "$pipe_out" 2>/dev/null

echo "Hello World!" > "$pipe_out"

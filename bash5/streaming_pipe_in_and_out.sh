pipe_in="$1"
pipe_out="$2"

tr '[:lower:]' '[:upper:]' < "$pipe_in" > "$pipe_out"

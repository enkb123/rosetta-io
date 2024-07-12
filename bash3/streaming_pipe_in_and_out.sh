#!/bin/bash
# Script reads text from a named pipe and writes it another named pipe, capitalized

pipe_in="$1"
pipe_out="$2"

cat "$pipe_in" | tr '[:lower:]' '[:upper:]' > "$pipe_out"

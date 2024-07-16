#!/bin/bash
# Script reads text from a named pipe and writes it another named pipe, capitalized

pipe_in="$1"
pipe_out="$2"

tr '[:lower:]' '[:upper:]' < "$pipe_in" > "$pipe_out"

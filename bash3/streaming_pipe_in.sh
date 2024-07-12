#!/bin/bash

# Script reads text from a named pipe and writes it to stdout, capitalized
pipe_in="$1"

cat "$pipe_in" | tr '[:lower:]' '[:upper:]'

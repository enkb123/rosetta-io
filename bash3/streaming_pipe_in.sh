#!/bin/bash

# Script reads text from a named pipe and writes it to stdout, capitalized
pipe_in="$1"

tr '[:lower:]' '[:upper:]' < "$pipe_in"

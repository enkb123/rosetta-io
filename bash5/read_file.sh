#!/bin/bash

# Read a file from file path (given as a command line arg),
# print line by line with line numbers

file_path="$1"

if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi

i=1

while IFS= read -r line; do
  echo "$((i++)) ${line^^}"
done < "$1"


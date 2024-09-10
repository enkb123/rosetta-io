#!/bin/bash

file_path="$1"

if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi

i=1

while IFS= read -r line; do
  echo "$((i++)) $(tr '[:lower:]' '[:upper:]' <<< "$line")"
done < "$file_path"

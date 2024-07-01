#!/bin/bash

# Script to read an argument and print as lowercase in stdout
file_path="$1"

if [ -z "$file_path" ]; then
  echo "Usage: $0 <file_path>"
  exit 1
fi

tr '[:upper:]' '[:lower:]' <<< "$file_path"

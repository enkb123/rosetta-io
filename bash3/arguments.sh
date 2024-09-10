#!/bin/bash

file_path="$1"

if [ -z "$file_path" ]; then
  echo "Usage: $0 <file_path>"
  exit 1
fi

tr '[:upper:]' '[:lower:]' <<< "$file_path"

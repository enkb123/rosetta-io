#!/bin/bash

# Script to decode Base64 text

encoded_string="$1"

if [ -z "$encoded_string" ]; then
  echo "Usage: $0 <encoded_string>"
  exit 1
fi

base64 -d <<< "$encoded_string"
echo  # tests expect a newline at the end

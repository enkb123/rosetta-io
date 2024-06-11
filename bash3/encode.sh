# Script to encode a string as Base64
#!/bin/bash

base64_encode() {
  local string="$1"
  local encoded
  encoded=$(printf "%s" "$string" | base64)
  echo "$encoded"
}

test_string="$1"

if [ -z "$test_string" ]; then
  echo "Usage: $0 <test_string>"
  exit 1
fi

# Encode string argument as string
encoded_string=$(base64_encode "$test_string")

echo "$encoded_string"


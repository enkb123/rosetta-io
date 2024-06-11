# Script to decode Base64 text

#!/bin/bash

encoded_string="$1"

if [ -z "$encoded_string" ]; then
  echo "Usage: $0 <encoded_string>"
  exit 1
fi

decoded_string=$(echo "$encoded_string" | base64 -d)

echo "$decoded_string"

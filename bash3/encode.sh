#!/bin/bash

# Script to encode a string as Base64

test_string="$1"

if [ -z "$test_string" ]; then
  echo "Usage: $0 <test_string>"
  exit 1
fi

echo -n "$test_string" | base64

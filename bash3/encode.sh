#!/bin/bash

test_string="$1"

if [ -z "$test_string" ]; then
  echo "Usage: $0 <test_string>"
  exit 1
fi

echo -n "$test_string" | base64

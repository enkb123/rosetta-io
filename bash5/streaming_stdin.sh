#!/bin/bash

# Script reads streaming input text and then prints capitalized string to stdout
while IFS= read -r input; do
  echo "${input^^}"
done

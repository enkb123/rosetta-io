# Script reads streaming input text and then prints capitalized string to stdout

#!/bin/bash

while IFS= read -r input; do
  echo "$input" | tr '[:lower:]' '[:upper:]'
done

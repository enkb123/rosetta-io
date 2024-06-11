# Test script to get input, transform, and write to stdout
#!/bin/bash
#!/bin/bash

i=1

while IFS= read -r user_input; do
  echo "$i $(echo "$user_input" | tr '[:lower:]' '[:upper:]')"
  ((i++))
done



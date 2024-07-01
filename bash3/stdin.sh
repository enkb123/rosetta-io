#!/bin/bash

# Test script to get input, transform, and write to stdout
#!/bin/bash

i=1

while IFS= read -r user_input; do
  echo "$((i++)) $(tr '[:lower:]' '[:upper:]' <<< "$user_input")"
done


# Script to write text to a new file
# Run script as `bash3 write_file.sh <output_file>.txt 'some text'`
#!/bin/bash

outfile="$1"
text="$2"

if [ -z "$outfile" ] || [ -z "$text" ]; then
  echo "Usage: $0 <output_file> <text>"
  exit 1
fi

echo -n "$text" | tr -d '\n' | tr '[:lower:]' '[:upper:]' > "$outfile"

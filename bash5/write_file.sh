outfile="$1"
text="$2"

if [ -z "$outfile" ] || [ -z "$text" ]; then
  echo "Usage: $0 <output_file> <text>"
  exit 1
fi

echo "${text^^}" > "$outfile"

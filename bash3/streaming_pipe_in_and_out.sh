input_file="streaming-in.pipe"
output_file="streaming-out.pipe"

exec 3> "$output_file"

while IFS= read -r line; do
    echo "received $line" >&3
done < "$input_file"

exec 3>&-

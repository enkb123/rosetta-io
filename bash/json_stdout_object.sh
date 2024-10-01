json_object='{}'

for arg in "$@"; do
    length=${#arg}
    json_object=$(<<<"$json_object" jo -f - "$arg=$length")
done

echo "$json_object"

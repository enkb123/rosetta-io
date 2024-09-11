json_objects=()

for arg in "$@"; do
    upper_arg=$(tr '[:lower:]' '[:upper:]' <<< "$arg")
    length=${#arg}
    json_objects+=("$(jo "$upper_arg"="$length")")
done

jo -a "${json_objects[@]}"

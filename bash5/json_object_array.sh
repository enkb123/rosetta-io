json_objects=()

for arg in "$@"; do
    json_objects+=("$(jo "${arg^^}"="${#arg}")")
done

jo -a "${json_objects[@]}"

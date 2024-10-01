lengths=()

for arg in "$@"; do
  lengths+=("${#arg}")
done

jo -a "${lengths[@]}"

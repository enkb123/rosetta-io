while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "line: $user_input"
done | tr '[:upper:]' '[:lower:]'

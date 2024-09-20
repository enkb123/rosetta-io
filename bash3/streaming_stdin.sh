while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "received $user_input"
done | tr '[:upper:]' '[:lower:]'

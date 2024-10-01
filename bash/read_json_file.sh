file_path="people.json"

jq -c '.[]' "$file_path" | while IFS= read -r person; do
    age=$(echo "$person" | jq -r '.age')
    first_name=$(echo "$person" | jq -r '.first_name')
    echo "Hello, $age year old $first_name"
done

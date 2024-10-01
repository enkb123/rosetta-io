file_path="./my-text-file.txt"

while IFS= read -r line; do
  echo "line: $line"

done < "$file_path"

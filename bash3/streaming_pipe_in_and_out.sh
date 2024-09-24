while IFS= read -r line; do
    echo "received $line"
done < streaming-in.pipe > streaming-out.pipe

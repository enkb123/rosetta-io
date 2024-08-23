#!/bin/bash

json_object='{}'

for arg in "$@"; do
    upper_chars=$(<<<"$arg" tr '[:lower:]' '[:upper:]' | fold -w1)

    json_array=$(jo -a ${upper_chars[@]})

    # merge this object with the current object
    json_object="$(<<<"$json_object" jo -f - "$arg"="$json_array")"
done

echo "$json_object"

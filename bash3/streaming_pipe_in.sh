#!/bin/bash
# Script reads text from a named pipe and writes it to stdout, capitalized


pipe_in="$1"

exec 3<> "$pipe_in"


is_readable() {
    local fd="$1"
    read line <&"$fd"
    echo "$line" | tr '[:lower:]' '[:upper:]'
}

while true; do
    if is_readable 3; then
        while read -r -u 3 line; do
            echo "$line" | tr '[:lower:]' '[:upper:]'
        done
    else
        sleep 0.1
    fi
done


exec 3>&-

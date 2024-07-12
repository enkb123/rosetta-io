#!/bin/bash
# Script reads text from a named pipe and writes it another named pipe, capitalized


pipe_in="$1"
pipe_out="$2"

exec 3<> "$pipe_in"

exec 4> "$pipe_out"

is_readable() {
    local fd="$1"
    read line <&"$fd"
    echo "$line" | tr '[:lower:]' '[:upper:]' >&4
}

while true; do
    if is_readable 3; then
        while read -r -u 3 line; do
            echo "$line" | tr '[:lower:]' '[:upper:]' >&4
        done
    else
        sleep 0.1
    fi
done


exec 3>&-
exec 4>&-

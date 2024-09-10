#!/bin/bash

i=1

while IFS= read -r user_input; do
  echo "$((i++)) $user_input"
done | tr '[:lower:]' '[:upper:]'

#!/bin/bash

for person in $(jq -c '.[]' <"$1"); do
  age="$(jq -r .age <<<"$person")"
  first_name="$(jq -r .first_name <<<"$person")"

  echo "Hello, $age year old $first_name"
done

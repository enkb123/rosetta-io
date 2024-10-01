# jo can't handle the null character (\0) so we use jq to add it as a workaraound
object_with_nonascii_string='{  }'

jo \
  true=true \
  false=false  \
  zero=0 \
  int=42 \
  float=3.14 \
  null=null \
  -s "empty string"="" \
  -s "a string with non-ascii characters"=$'hello \n \1 world 🥸'

jo \
  "array of strings=$(
    jo -a abc def ghi jkl
  )" \
  "array of numbers=$(
    jo -a 13 42 9000 -7
  )" \
  "array of nothing=$(
    jo -a </dev/null
  )" \
  "array of mixed=$(
    jo -a 13 def null false "$(jo -a a)" "$(jo o=1)"
  )" \
  "array of objects=$(
    jo -a \
      "$(jo name="Bob Barker" age=84)" \
      "$(jo address1="123 Main St" address2="Apt 1")"
  )" \
  "array of arrays=$(
    jo -a \
      "$(jo -a a b c)" \
      "$(jo -a d e f)"
  )"

jo objects="$(
  jo nested="$(
    jo objects="$(
      jo are="supported"
    )"
  )"
)"

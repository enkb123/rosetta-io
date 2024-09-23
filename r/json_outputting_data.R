library(jsonlite)

first_json_object <- list(
  true = TRUE,
  false = FALSE,
  zero = 0,
  int = 42,
  float = 3.14,
  null = NA,
  "empty string" = "",
  # b/c R can't handle the null character in strings, we use @NULL@ to represent
  # it then replace it with the actual JSON-encoded null character later
  "a string with non-ascii characters" = "hello \n @NULL@ \u0001 world 🥸"
)

second_json_object <- list(
  "array of strings" = c("abc", "def", "ghi", "jkl"),
  "array of numbers" = c(13, 42, 9000, -7),
  "array of nothing" = list(),
  "array of mixed" = list(13, "def", NA, FALSE, list("a"), list(o = 1)),
  "array of objects" = list(
    list(name = "Bob Barker", age = 84),
    list(address1 = "123 Main St", address2 = "Apt 1")
  ),
  "array of arrays" = list(
    c("a", "b", "c"),
    c("d", "e", "f")
  )
)

third_json_object <- list(
  objects = list(
    nested = list(
      objects = list(
        are = "supported"
      )
    )
  )
)

first_json_string <- gsub("@NULL@", "\\\\u0000", toJSON(first_json_object, auto_unbox = TRUE, pretty = FALSE))
second_json_string <- toJSON(second_json_object, auto_unbox = TRUE, pretty = FALSE)
third_json_string <- toJSON(third_json_object, auto_unbox = TRUE, pretty = FALSE)

cat(first_json_string, "\n")
cat(second_json_string, "\n")
cat(third_json_string, "\n")

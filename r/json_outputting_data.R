library(jsonlite)

# Define the first JSON object
first_json_object <- list(
  true = TRUE,
  false = FALSE,
  zero = 0,
  int = 42,
  float = 3.14,
  null = NULL,
  empty_string = "",
  a_string_with_non_ascii_characters = "hello \n \0 \u0001 world 🥸"  # Make sure the escape sequence is correct
)

# Define the second JSON object
second_json_object <- list(
  array_of_strings = c("abc", "def", "ghi", "jkl"),
  array_of_numbers = c(13, 42, 9000, -7),
  array_of_nothing = list(),  # Should be an empty list
  array_of_mixed = list(13, "def", NULL, FALSE, c("a"), list(o = 1)),
  array_of_objects = list(
    list(name = "Bob Barker", age = 84),
    list(address1 = "123 Main St", address2 = "Apt 1")
  ),
  array_of_arrays = list(
    c("a", "b", "c"),
    c("d", "e", "f")
  )
)

# Define the third JSON object
third_json_object <- list(
  objects = list(
    nested = list(
      objects = list(
        are = "supported"
      )
    )
  )
)

# Convert the R lists to JSON strings and print them
cat(toJSON(first_json_object, auto_unbox = TRUE, pretty = FALSE), "\n")
cat(toJSON(second_json_object, auto_unbox = TRUE, pretty = FALSE), "\n")
cat(toJSON(third_json_object, auto_unbox = TRUE, pretty = FALSE), "\n")

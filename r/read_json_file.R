library(jsonlite)

filename <- "people.json"

people <- fromJSON(filename, simplifyVector = FALSE)

for (person in people) {
    cat("Hello,", person$age, "year old", person$first_name, "\n")
}

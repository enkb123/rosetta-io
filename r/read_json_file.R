library(jsonlite)

filename <- "people.json"

people <- fromJSON(filename)

for (i in 1:nrow(people)){
    cat(paste0("Hello, ", people$age[i], " year old ", people$first_name[i], "\n"))
}

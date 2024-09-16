library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

people <- fromJSON(args[1])

for (i in 1:nrow(people)){
    cat(paste0("Hello, ", people$age[i], " year old ", people$first_name[i], "\n"))
}

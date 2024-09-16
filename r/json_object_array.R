library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

myArray <- list()
for (arg in args) {
    string_length <- list()
    string_length[[toupper(arg)]] <- nchar(arg)
    myArray[[length(myArray)+1]] <- string_length
}

cat(toJSON(myArray, auto_unbox=TRUE))

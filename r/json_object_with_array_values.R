library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

string_letters <- list()
for (string in args) {
  letters <- toupper(strsplit(string, split="")[[1]])
  string_letters[[string]] <- letters
}

cat(toJSON(string_letters))

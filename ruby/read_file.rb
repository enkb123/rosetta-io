# Read a file from file path (given as a command line arg),
# print line by line with line numbers

File.open("./my-text-file.txt", "r") do |f|
  f.each_line do |line|
    puts "line: #{line}"
  end
end

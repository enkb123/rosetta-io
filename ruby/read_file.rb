File.open("./my-text-file.txt", "r") do |f|
  f.each_line do |line|
    puts "line: #{line}"
  end
end

STDOUT.sync = true # turn off buffering on stdout

File.each_line "input.pipe" do |line|
  puts line.upcase
end

STDOUT.sync = true # turn off buffering on stdout

File.foreach 'input.pipe' do |line|
  puts line.upcase
end

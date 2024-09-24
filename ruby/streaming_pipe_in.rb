STDOUT.sync = true

File.foreach 'input.pipe' do |line|
  puts line.upcase
end

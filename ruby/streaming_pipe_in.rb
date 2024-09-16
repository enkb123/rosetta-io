STDOUT.sync = true

File.open 'input.pipe', 'r' do |pipe|
  pipe.each_line do |line|
    puts line.upcase
  end
end

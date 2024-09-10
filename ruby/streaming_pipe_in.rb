STDOUT.sync = true

pipe_in = ARGV.fetch(0)

File.open(pipe_in, 'r') do |pipe|
  pipe.each_line do |line|
    puts line.upcase
  end
end

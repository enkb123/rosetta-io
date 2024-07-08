# Script reads text from a named pipe and writes it to stdout, capitalized

STDOUT.sync = true

pipe_in = ARGV.fetch(0)

File.open(pipe_in, 'r') do |pipe|
  pipe.each_line do |line|
    puts line.upcase
  end
end

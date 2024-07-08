# Script reads text from a named pipe and writes it to stdout, capitalized

STDOUT.sync = true

fifo_name = ARGV.fetch(0)

File.open(fifo_name, 'r') do |pipe|
  pipe.each_line do |line|
    puts line.upcase
  end
end

# Script reads text from a named pipe and writes it another named pipe, capitalized

pipe_in, pipe_out = ARGV

File.open(pipe_out, 'w') do |output|
  output.sync = true

  File.open(pipe_in, 'r') do |input|
    input.each_line do |line|
      output.puts line.upcase
    end
  end
end

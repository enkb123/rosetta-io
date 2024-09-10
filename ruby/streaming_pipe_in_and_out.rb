# Script reads text from a named pipe and writes it another named pipe, capitalized

File.open 'streaming-out.pipe', 'w' do |output|
  output.sync = true

  File.open 'streaming-in.pipe', 'r' do |input|
    input.each_line do |line|
      output.puts "received #{line}"
    end
  end
end

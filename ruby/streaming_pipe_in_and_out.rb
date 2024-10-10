File.open 'streaming-out.pipe', 'w' do |output|
  output.sync = true # turn off buffering on the ouput pipe

  File.foreach "streaming-in.pipe" do |line|
    output.puts "received #{line}"
  end
end

File.open 'streaming-out.pipe', 'w' do |output|
  output.sync = true

  File.foreach "streaming-in.pipe" do |line|
    output.puts "received #{line}"
  end
end

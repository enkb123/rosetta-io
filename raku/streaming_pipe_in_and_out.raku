use v6;

my $output = open 'streaming-out.pipe', :w;
my $input = open 'streaming-in.pipe', :r;

$output.say("received $_") for $input.lines;

$output.close;
$input.close;

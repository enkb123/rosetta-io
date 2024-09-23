use v6;

my $input-file = 'streaming-in.pipe';
my $output-file = 'streaming-out.pipe';

my $output = open $output-file, :w;

my $input = open $input-file, :r;

for $input.lines -> $line {
    $output.say("received $line");
}

$output.close;
$input.close;

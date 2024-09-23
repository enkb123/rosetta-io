use strict;
use warnings;

my $input_file = 'streaming-in.pipe';
my $output_file = 'streaming-out.pipe';


open my $output, '>', $output_file or die "Cannot open output pipe: $!";
open my $input, '<', $input_file or die "Cannot open input pipe: $!";

$output->autoflush(1);

while (my $line = <$input>) {
    print $output "received $line";
}

close $input;
close $output;

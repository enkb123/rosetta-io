use strict;
use warnings;

my ($pipe_in, $pipe_out) = @ARGV;

open my $output, '>', $pipe_out or die "Cannot open output pipe: $!";
open my $input, '<', $pipe_in or die "Cannot open input pipe: $!";

$output->autoflush(1);

while (my $line = <$input>) {
    print $output uc($line);
}

close $input;
close $output;

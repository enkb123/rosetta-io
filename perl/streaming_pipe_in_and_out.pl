use strict;
use warnings;

open my $output, '>', 'streaming-out.pipe';
open my $input, '<', 'streaming-in.pipe';

$output->autoflush(1); # turn off buffering on output pipe

print $output "received $_" while <$input>;

close $input;
close $output;

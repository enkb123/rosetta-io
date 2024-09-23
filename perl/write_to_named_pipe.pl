use strict;
use warnings;

my $pipe_path = 'output.pipe';

system("mkfifo $pipe_path") unless -e $pipe_path;

open(my $pipe, '>', $pipe_path) or die "Could not open '$pipe_path': $!";

print $pipe "Hello World!\n";

close($pipe);

# Script reads text from a named pipe and writes it another named pipe, capitalized
use v6;

my ($pipe_in, $pipe_out) = @*ARGS;

my $output = open($pipe_out, :w);
my $input = open($pipe_in, :r);

for $input.lines {
    $output.print(.uc ~ "\n");
}

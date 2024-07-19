use v6;

my $pipe_in = @*ARGS[0];

my $input = open($pipe_in, :r);

for $input.lines() {
    say .uc;
}

$input.close;

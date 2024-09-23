use v6;

my $pipe_in = "input.pipe";

my $input = open($pipe_in, :r);

for $input.lines() {
    say .uc;
    $*OUT.flush;
}

$input.close;

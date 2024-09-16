use v6;

my $file-path = @*ARGS.shift;
my $fh = open $file-path, :r;

my $i = 1;
for $fh.lines {
    say $i++ ~ " " ~ .uc;
}

$fh.close;

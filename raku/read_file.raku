# Read a file from file path (given as a command line arg),
# print line by line with line numbers

use v6;

my $file-path = @*ARGS.shift;
my $fh = open $file-path, :r;

my $i = 1;
for $fh.lines {
    say $i++ ~ " " ~ .uc;
}

$fh.close;

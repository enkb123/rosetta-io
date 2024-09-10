use v6;

my ($outfile, $text) = @*ARGS;

my $fh = open $outfile, :w;

$fh.print: $text.uc;
$fh.close;

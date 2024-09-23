use v6;

my ($outfile, $text) = ("output.txt", "Hello World!");

my $fh = open $outfile, :w;

$fh.print: $text;
$fh.close;

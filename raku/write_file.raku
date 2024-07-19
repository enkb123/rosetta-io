# Script to write text to a new file
# Run script as `perl write_file.pl <output_file>.txt 'some text'`
use v6;

my ($outfile, $text) = @*ARGS;

my $fh = open $outfile, :w;

$fh.print: $text.uc;
$fh.close;

use v6;

my $fh = open "output.txt", :w;
$fh.print: "Hello World!";
$fh.close;

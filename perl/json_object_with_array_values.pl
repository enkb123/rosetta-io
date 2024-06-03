use strict;
use warnings;
use JSON;

# Get command line arguments
my @my_strings = @ARGV;

# Create a hash to store strings as keys and arrays of letters as values
my %string_letters_dict;

# Populate the hash
foreach my $string (@my_strings) {
    my @letters = split //, uc($string);
    $string_letters_dict{$string} = \@letters;
}
# Convert the hash to JSON and print to STDOUT
print JSON->new->canonical(1)->encode(\%string_letters_dict);

# Script outputs arrays of objects as JSON
use strict;
use warnings;
use JSON;

# Get command line arguments
my @my_strings = @ARGV;

# Create an array to store dictionaries
my @my_array;

# Populate the array with dictionaries
foreach my $string (@my_strings) {
    my %dict = (uc($string) => length($string));
    push @my_array, \%dict;
}

# Convert the array of dictionaries to JSON and print to STDOUT
print JSON->new->canonical(1)->encode(\@my_array);

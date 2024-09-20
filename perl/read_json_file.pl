use strict;
use warnings;
use JSON;

my $file_path = 'people.json';

my $json_string;
{
    local $/;
    open my $fh, '<', $file_path;
    $json_string = <$fh>;
    close $fh;
}

my $people = decode_json($json_string);

foreach my $person (@$people) {
    my $age = $person->{age};
    my $first_name = $person->{first_name};
    print "Hello, $age year old $first_name\n";
}

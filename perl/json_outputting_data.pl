use strict;
use warnings;
use JSON;

my $json = JSON->new->utf8;

my $data1 = {
    "true" => JSON::true,
    "false" => JSON::false,
    "zero" => 0,
    "int" => 42,
    "float" => 3.14,
    "null" => undef,
    "empty string" => "",
    "a string with non-ascii characters" => "hello \n \x{0001} world \N{U+1F978}",
};

print $json->encode($data1) . "\n";

my $data2 = {
    "array of strings" => ["abc", "def", "ghi", "jkl"],
    "array of numbers" => [13, 42, 9000, -7],
    "array of nothing" => [],
    "array of mixed" => [13, "def", undef, JSON::false, ["a"], { "o" => 1 }],
    "array of objects" => [
        { "name" => "Bob Barker", "age" => 84 },
        { "address1" => "123 Main St", "address2" => "Apt 1" },
    ],
    "array of arrays" => [
        ["a", "b", "c"],
        ["d", "e", "f"],
    ],
};

print $json->encode($data2) . "\n";

my $data3 = {
    "objects" => { "nested" => { "objects" => { "are" => "supported" } } },
};

print $json->encode($data3) . "\n";

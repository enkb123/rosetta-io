use v6;
use JSON::Fast;

my %data = @*ARGS.map: { $_ => .chars };
say to-json(%data);

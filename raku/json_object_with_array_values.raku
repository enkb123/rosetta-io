
use v6;
use JSON::Fast;

my %data = @*ARGS.map: { $_ => [ .uc.comb ] };
say to-json(%data);

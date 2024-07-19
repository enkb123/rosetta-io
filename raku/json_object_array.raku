# Script outputs arrays of objects as JSON
use v6;
use JSON::Fast;

say to-json(@*ARGS.map: { uc($_) => $_.chars });

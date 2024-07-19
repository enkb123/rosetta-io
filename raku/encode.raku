use v6;
use MIME::Base64;

say MIME::Base64.encode-str(@*ARGS[0]);

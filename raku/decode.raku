use v6;
use MIME::Base64;

say MIME::Base64.decode-str(@*ARGS[0]);

<?php

$stringToEncode = $argv[1];

$encodedString = base64_encode($stringToEncode);

echo $encodedString;

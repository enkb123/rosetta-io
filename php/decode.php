<?php

$encodedString = $argv[1];

$decodedString = base64_decode($encodedString);

echo $decodedString;

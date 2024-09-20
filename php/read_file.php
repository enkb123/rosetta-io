<?php

$filePath = './my-text-file.txt';
$file = fopen($filePath, 'r');

while (($line = fgets($file)) !== false) {
    $line = trim($line);
    echo "line: $line\n";
}

fclose($file);

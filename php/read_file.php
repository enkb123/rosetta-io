<?php

$file_path = './my-text-file.txt';
$file = fopen($file_path, 'r');

foreach (file($file_path) as $index => $line) {
    echo "line: $line";
}

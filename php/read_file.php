<?php

$file_path = './my-text-file.txt';

foreach (file($file_path) as $index => $line) {
    echo "line: $line";
}

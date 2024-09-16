<?php

$file_path = $argv[1];

$file = fopen($file_path, 'r');

foreach (file($file_path) as $index => $line) {
    echo ($index + 1) . ' ' . strtoupper($line);
}

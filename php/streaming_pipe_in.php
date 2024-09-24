<?php

$input_pipe = fopen("input.pipe", 'r');

while (($line = fgets($input_pipe)) !== false) {
    echo strtoupper($line);
}

fclose($input_pipe);

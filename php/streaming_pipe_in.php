<?php

$pipe_in = $argv[1];

$input_pipe = fopen($pipe_in, 'r');

while (($line = fgets($input_pipe)) !== false) {
    echo strtoupper($line);
}

fclose($input_pipe);

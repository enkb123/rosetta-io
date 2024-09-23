<?php

$pipe_in = "input.pipe";

$input_pipe = fopen($pipe_in, 'r');

while (($line = fgets($input_pipe)) !== false) {
    echo strtoupper($line);
}

fclose($input_pipe);

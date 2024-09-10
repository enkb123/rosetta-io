<?php

$i = 1;

while ($user_input = fgets(STDIN)) {
    echo $i++ . ' ' . strtoupper($user_input);
}

<?php

$jsonFile = $argv[1];

$jsonData = file_get_contents($jsonFile);

$people = json_decode($jsonData);

foreach ($people as $person) {
    echo "Hello, {$person->age} year old {$person->first_name}\n";
}

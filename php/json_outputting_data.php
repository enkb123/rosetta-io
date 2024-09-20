<?php

$firstJsonObject = [
    "true" => true,
    "false" => false,
    "zero" => 0,
    "int" => 42,
    "float" => 3.14,
    "null" => null,
    "empty string" => "",
    "a string with non-ascii characters" => "hello \n \0 \x01 world 🥸"
];

$secondJsonObject = [
    "array of strings" => ["abc", "def", "ghi", "jkl"],
    "array of numbers" => [13, 42, 9000, -7],
    "array of nothing" => [],
    "array of mixed" => [13, "def", null, false, ["a"], ["o" => 1]],
    "array of objects" => [
        ["name" => "Bob Barker", "age" => 84],
        ["address1" => "123 Main St", "address2" => "Apt 1"]
    ],
    "array of arrays" => [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
];

$thirdJsonObject = [
    "objects" => [
        "nested" => [
            "objects" => [
                "are" => "supported"
            ]
        ]
    ]
];

echo json_encode($firstJsonObject, JSON_UNESCAPED_UNICODE) . "\n";
echo json_encode($secondJsonObject, JSON_UNESCAPED_UNICODE) . "\n";
echo json_encode($thirdJsonObject, JSON_UNESCAPED_UNICODE) . "\n";
?>

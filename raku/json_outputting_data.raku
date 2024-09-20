use JSON::Fast;

my %first_json_object = Hash.new(
    'true'                    => True,
    'false'                   => False,
    'zero'                    => 0,
    'int'                     => 42,
    'float'                   => 3.14,
    'null'                    => Nil,
    'empty string'            => '',
    'a string with non-ascii characters' => "hello \n \0 \x01 world 🥸"
);

my %second_json_object = Hash.new(
    'array of strings' => ['abc', 'def', 'ghi', 'jkl'],
    'array of numbers' => [13, 42, 9000, -7],
    'array of nothing' => [],
    'array of mixed'   => [13, 'def', Nil, False, ['a'], Hash.new('o' => 1)],
    'array of objects' => [
        Hash.new('name' => 'Bob Barker', 'age' => 84),
        Hash.new('address1' => '123 Main St', 'address2' => 'Apt 1')
    ],
    'array of arrays' => [
        ['a', 'b', 'c'],
        ['d', 'e', 'f']
    ]
);

my %third_json_object = Hash.new(
    'objects' => Hash.new(
        'nested' => Hash.new(
            'objects' => Hash.new(
                'are' => 'supported'
            )
        )
    )
);

say to-json(%first_json_object, :pretty(False));
say to-json(%second_json_object, :pretty(False));
say to-json(%third_json_object, :pretty(False));

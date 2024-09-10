// Script takes string arguments and outputs a JSON array of numbers representing
// the length of each argument
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonNumbers
{
    public static void Main(string[] args)
    {
        var numbers = args.Select(arg => arg.Length).ToArray();

        string jsonArrayString = JsonSerializer.Serialize(numbers);
        Console.WriteLine(jsonArrayString);
    }
}

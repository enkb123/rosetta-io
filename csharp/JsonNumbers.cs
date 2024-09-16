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

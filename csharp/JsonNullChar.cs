using System;
using System.Collections.Generic;
using System.Text.Json;

class JsonNullChar
{
    public static void Main(string[] args)
    {
        Console.WriteLine(JsonSerializer.Serialize("Hello World \0"));
    }
}

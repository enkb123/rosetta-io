using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonObjectArray
{
    public static void Main(string[] args)
    {
        var jsonObjects = args.Select(str => new Dictionary<string, object> {
            { str.ToUpper(), str.Length }
        }).ToList();
        string jsonArrayString = JsonSerializer.Serialize(jsonObjects);
        Console.WriteLine(jsonArrayString);
    }
}

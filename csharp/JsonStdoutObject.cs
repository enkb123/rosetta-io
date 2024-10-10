using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonStdoutObject
{
    public static void Main(string[] args)
    {
        var stringLengthDict = new Dictionary<string, int>();

        foreach (string str in args)
        {
            stringLengthDict[str] = str.Length;
        }

        string jsonString = JsonSerializer.Serialize(stringLengthDict);
        Console.WriteLine(jsonString);
    }
}

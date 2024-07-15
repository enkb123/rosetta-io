// Script takes arguments and transforms them into dict with arrays as dict values and returns as JSON

using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonObjectWithArrayValues{
    public static void Main(string[] args){
        var jsonObject = args.ToDictionary(
            str => str,
            str => str.ToUpper().Select(c => c.ToString()).ToList()
        );

        string jsonString = JsonSerializer.Serialize(jsonObject);
        Console.WriteLine(jsonString);
    }
}

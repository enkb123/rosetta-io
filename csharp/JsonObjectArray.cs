// Script outputs arrays of objects as JSON
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonObjectArray
{
    public static void Main(string[] args){
        List<object> jsonObjects = new List<object>();

        foreach (string str in args){
            var jsonObject = new Dictionary<string, object>{
                { str.ToUpper(), str.Length }
            };
            jsonObjects.Add(jsonObject);
        }
        string jsonArrayString = JsonSerializer.Serialize(jsonObjects);
        Console.WriteLine(jsonArrayString);
    }
}

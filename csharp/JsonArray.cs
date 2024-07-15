//Script takes args and turns into JSON array

using System;
using System.Text.Json;

class JsonArray{
    public static void Main(string[] args){
        string[] inputArray = args;

        string jsonString = JsonSerializer.Serialize(inputArray);

        Console.WriteLine(jsonString);
    }
}


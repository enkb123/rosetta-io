//Script takes control characters and outputs valid JSON
using System;
using System.Text.Json;

public class JsonControlChars{
    public static void Main(string[] args){
        string testString = args[0];
        string jsonString = JsonSerializer.Serialize(testString);

        Console.WriteLine(jsonString);
    }
}


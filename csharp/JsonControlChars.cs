using System;
using System.Text.Json;

class JsonControlChars{
    public static void Main(string[] args){
        string testString = args[0];
        string jsonString = JsonSerializer.Serialize(testString);

        Console.WriteLine(jsonString);
    }
}

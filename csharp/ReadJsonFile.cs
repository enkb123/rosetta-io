using System;
using System.IO;
using System.Text.Json;

class ReadJsonFile
{
    public static void Main(string[] args)
    {
        var filePath = "people.json";

        var json = File.ReadAllText(filePath);

        var people = JsonSerializer.Deserialize<JsonElement[]>(json);

        foreach (var person in people)
        {
            var age = person.GetProperty("age").GetInt32();
            var firstName = person.GetProperty("first_name").GetString();
            Console.WriteLine($"Hello, {age} year old {firstName}");
        }
    }
}

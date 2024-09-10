// Read JSON file, transform and print to stdout
using System;
using System.IO;
using System.Text.Json;

class ReadJsonFile{
    public static void Main(string[] args){
        string jsonFilePath = args[0];
        string jsonContent = File.ReadAllText(jsonFilePath);

        JsonElement root = JsonDocument.Parse(jsonContent).RootElement;

        foreach (JsonElement person in root.EnumerateArray()){
            long age = person.GetProperty("age").GetInt64();
            string firstName = person.GetProperty("first_name").GetString();
            Console.WriteLine($"Hello, {age} year old {firstName}");
        }
    }
}

// Read JSON file, transform and print to stdout
using System;
using System.IO;
using System.Text.Json;

public class ReadJsonFile{
    public static void Main(string[] args){
        string jsonFilePath = args[0];
        string jsonContent = File.ReadAllText(jsonFilePath);

        JsonDocument doc = JsonDocument.Parse(jsonContent);
        JsonElement root = doc.RootElement;

        foreach (JsonElement person in root.EnumerateArray()){
            if (person.ValueKind == JsonValueKind.Object){
                if (person.TryGetProperty("age", out JsonElement ageElement) && ageElement.ValueKind == JsonValueKind.Number &&
                    person.TryGetProperty("first_name", out JsonElement firstNameElement) && firstNameElement.ValueKind == JsonValueKind.String)
                {
                    long age = ageElement.GetInt64();
                    string firstName = firstNameElement.GetString();
                    Console.WriteLine($"Hello, {age} year old {firstName}");
                }
            }
        }
    }
}


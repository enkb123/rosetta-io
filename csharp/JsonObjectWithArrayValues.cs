// Script takes arguments and transforms them into dict with arrays as dict values and returns as JSON

using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonObjectWithArrayValues{
    public static void Main(string[] args){
        Dictionary<string, List<string>> jsonObject = new Dictionary<string, List<string>>();

        foreach (string str in args){
            List<string> lettersArray = new List<string>();
            foreach (char c in str.ToUpper()){
                lettersArray.Add(c.ToString());
            }
            jsonObject[str] = lettersArray;
        }

        string jsonString = JsonSerializer.Serialize(jsonObject);
        Console.WriteLine(jsonString);
    }
}

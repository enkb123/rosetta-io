// Script takes arguments and transforms them into dict with arrays as dict values
// and returns as JSON

using System;
using System.Collections.Generic;
using System.Text;

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

        StringBuilder sb = new StringBuilder("{");

        int count = 0;
        foreach (var kvp in jsonObject){
            if (count > 0){
                sb.Append(", ");
            }
            sb.Append($"\"{kvp.Key}\": [\"{string.Join("\", \"", kvp.Value)}\"]");
            count++;
        }

        sb.Append("}");

        string jsonString = sb.ToString();

        Console.WriteLine(jsonString);
    }
}


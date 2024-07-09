// Script reads string args and transforms into python dict

using System;
using System.Collections.Generic;
using System.Text;

public class JsonStdoutObject
{
    public static void Main(string[] args)
    {
        Dictionary<string, int> stringLengthDict = new Dictionary<string, int>();

        foreach (string str in args)
        {
            stringLengthDict[str] = str.Length;
        }

        StringBuilder sb = new StringBuilder("{");

        int count = 0;
        foreach (var kvp in stringLengthDict)
        {
            if (count > 0)
            {
                sb.Append(", ");
            }
            sb.Append($"\"{kvp.Key}\": {kvp.Value}");
            count++;
        }

        sb.Append("}");

        string jsonString = sb.ToString();

        Console.WriteLine(jsonString);
    }
}

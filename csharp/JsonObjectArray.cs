// Script outputs arrays of objects as JSON

using System;
using System.Collections.Generic;
using System.Text;

class JsonObjectArray{
    public static void Main(string[] args){
        StringBuilder sb = new StringBuilder("[");
        int count = 0;

        foreach (string str in args){
            if (count > 0){
                sb.Append(", ");
            }

            sb.Append($"{{ \"{str.ToUpper()}\": {str.Length} }}");
            count++;
        }

        sb.Append("]");

        string jsonArrayString = sb.ToString();

        Console.WriteLine(jsonArrayString);
    }
}

// Script takes string arguments and outputs a JSON array of numbers representing
// the length of each argument
using System;
using System.Text;

public class JsonNumbers
{
    public static void Main(string[] args)
    {

        StringBuilder sb = new StringBuilder("[");

        for (int i = 0; i < args.Length; i++)
        {
            if (i > 0)
            {
                sb.Append(", ");
            }
            sb.Append(args[i].Length);
        }

        sb.Append("]");

        string jsonArrayString = sb.ToString();

        Console.WriteLine(jsonArrayString);
    }
}

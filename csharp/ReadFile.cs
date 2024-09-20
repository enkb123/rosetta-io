using System;
using System.IO;

class ReadFile
{
    public static void Main(string[] args)
    {
        string filePath = "./my-text-file.txt";
        using (StreamReader reader = new StreamReader(filePath))
        {
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine($"line: {line}");
            }
        }
    }
}

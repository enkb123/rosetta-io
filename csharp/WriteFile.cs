//Script to write text to a new file
//Run script as `csharp write_file.cs <output_file>.txt 'some text'`

using System;
using System.IO;

public class WriteFile
{
    public static void Main(string[] args)
    {
        if (args.Length != 2)
        {
            Console.Error.WriteLine("Usage: WriteFile.exe <output_file>.txt 'some text'");
            Environment.Exit(1);
        }

        string outFile = args[0];
        string text = args[1].ToUpper();

        try
        {
            File.WriteAllText(outFile, text);
        }
        catch (IOException e)
        {
            Console.Error.WriteLine($"Error writing to {outFile}: {e.Message}");
            Environment.Exit(1);
        }
    }
}


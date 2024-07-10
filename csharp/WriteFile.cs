//Script to write text to a new file
//Run script as `csharp write_file.cs <output_file>.txt 'some text'`

using System;
using System.IO;

public class WriteFile
{
    public static void Main(string[] args)
    {
        string outFile = args[0];
        string text = args[1].ToUpper();

        File.WriteAllText(outFile, text);
    }
}

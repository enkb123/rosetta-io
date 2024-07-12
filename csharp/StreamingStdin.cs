// Script reads streaming input text and then prints capitalized string to stdout

using System;

class StreamingStdin{
    public static void Main(string[] args){
        string line;

        while (!string.IsNullOrEmpty(line = Console.ReadLine())){
            Console.WriteLine(line.ToUpper());
        }
    }
}

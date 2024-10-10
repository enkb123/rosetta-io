using System;

class StreamingStdin
{
    public static void Main(string[] args)
    {
        string line;

        while (!string.IsNullOrEmpty(line = Console.ReadLine()))
        {
            Console.WriteLine($"received {line}");
        }
    }
}

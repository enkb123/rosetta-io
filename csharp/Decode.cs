//Script to decode Base64 text
using System;

class Decode{
    public static void Main(string[] args){
        string encodedString = args[0];

        byte[] decodedBytes = Convert.FromBase64String(encodedString);
        string decodedString = System.Text.Encoding.UTF8.GetString(decodedBytes);

        Console.WriteLine(decodedString);
    }
}

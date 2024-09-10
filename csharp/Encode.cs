//Script to encode a string as Base64

using System;

class Encode{
    public static void Main(string[] args){
        string testString = args[0];
        string encodedString = Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(testString));
        Console.WriteLine(encodedString);
    }
}

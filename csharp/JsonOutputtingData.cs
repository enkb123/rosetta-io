using System;
using System.Collections.Generic;
using System.Text.Json;

class JsonOutputtingData
{
    public static void Main(string[] args)
    {
        var firstJsonObject = new Dictionary<string, object> {
            ["true"] = true,
            ["false"] = false,
            ["zero"] = 0,
            ["int"] = 42,
            ["float"] = 3.14,
            ["null"] = (object)null,
            ["empty string"] = "",
            ["a string with non-ascii characters"] = "hello \n \0 \u0001 world 🥸"
        };

        var secondJsonObject = new Dictionary<string, object> {
            ["array of strings"] = new[] { "abc", "def", "ghi", "jkl" },
            ["array of numbers"] = new[] { 13, 42, 9000, -7 },
            ["array of nothing"] = Array.Empty<object>(),
            ["array of mixed"] = new object[] { 13, "def", null, false, new[] { "a" }, new Dictionary<string, object> { ["o"] = 1 } },
            ["array of objects"] = new[]
            {
                new Dictionary<string, object>
                {
                    ["name"] = "Bob Barker",
                    ["age"] = 84
                },
                new Dictionary<string, object> {
                    ["address1"] = "123 Main St",
                    ["address2"] = "Apt 1"
                }
            },
            ["array of arrays"] = new[] {
                new[] { "a", "b", "c" },
                new[] { "d", "e", "f" }
            }
        };

        var thirdJsonObject = new Dictionary<string, object>
        {
            ["objects"] = new Dictionary<string, object>
            {
                ["nested"] = new Dictionary<string, object>
                {
                    ["objects"] = new Dictionary<string, object>
                    {
                        ["are"] = "supported"
                    }
                }
            }
        };

        Console.WriteLine(JsonSerializer.Serialize(firstJsonObject));
        Console.WriteLine(JsonSerializer.Serialize(secondJsonObject));
        Console.WriteLine(JsonSerializer.Serialize(thirdJsonObject));
    }
}

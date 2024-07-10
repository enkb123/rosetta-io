//Script takes args and turns into JSON array

using System;
using System.Text;

class JsonArray{
    public static void Main(string[] args){
        StringBuilder sb = new StringBuilder("[");

        for (int i = 0; i < args.Length; i++){
            if (i > 0){
                sb.Append(", ");
            }
            sb.Append('"').Append(args[i]).Append('"');
        }

        sb.Append("]");

        Console.WriteLine(sb.ToString());
    }
}

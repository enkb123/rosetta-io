// Script takes string arguments and outputs a JSON array of numbers representing
// the length of each argument
import org.json.simple.JSONArray;

public class JsonNumbers {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java StringLengthToJson <string1> <string2> ...");
            System.exit(1);
        }

        JSONArray jsonArray = new JSONArray();
        for (String str : args) {
            jsonArray.add(str.length());
        }

        System.out.println(jsonArray.toJSONString());
    }
}

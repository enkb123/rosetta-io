//Script takes control characters and outputs valid JSON
import org.json.simple.JSONValue;

public class JsonControlChars {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java JsonControlChars.java <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        String jsonString = JSONValue.toJSONString(testString);
        System.out.println(jsonString);
    }
}


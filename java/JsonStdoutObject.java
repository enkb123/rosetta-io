// Script reads string args and transforms into python dict

import java.util.HashMap;
import java.util.Map;

public class JsonStdoutObject {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java JsonStdoutObject.java <string1> <string2> ...");
            System.exit(1);
        }

        var stringLengthDict = new HashMap<String, Integer>();

        for (String string : args) {
            stringLengthDict.put(string, string.length());
        }

        StringBuilder jsonStringBuilder = new StringBuilder("{");
        for (Map.Entry<String, Integer> entry : stringLengthDict.entrySet()) {
            jsonStringBuilder.append("\"").append(entry.getKey()).append("\":").append(entry.getValue()).append(",");
        }
        jsonStringBuilder.deleteCharAt(jsonStringBuilder.length() - 1); // Remove trailing comma
        jsonStringBuilder.append("}");

        String jsonString = jsonStringBuilder.toString();

        System.out.println(jsonString);
    }
}

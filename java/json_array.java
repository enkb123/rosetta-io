//Script takes args and turns into JSON array

import org.json.simple.JSONArray;

public class StringToJsonArray {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java StringToJsonArray <string1> <string2> ...");
            System.exit(1);
        }

        JSONArray jsonArray = new JSONArray();
        for (String arg : args) {
            jsonArray.add(arg);
        }

        System.out.println(jsonArray.toJSONString());
    }
}

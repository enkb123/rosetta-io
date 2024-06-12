// Script takes arguments and transforms them into dict with arrays as dict values
// and returns as JSON
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import java.util.Arrays;

public class JsonObjectWithArrayValues {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java StringToDict <string1> <string2> ...");
            System.exit(1);
        }

        JSONObject jsonObject = new JSONObject();
        for (String str : args) {
            JSONArray charArray = new JSONArray();
            Arrays.stream(str.toUpperCase().split("")).forEach(charArray::add);
            jsonObject.put(str, charArray);
        }

        System.out.println(jsonObject.toString());
    }
}

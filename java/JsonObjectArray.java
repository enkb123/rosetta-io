// Script outputs arrays of objects as JSON

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public class JsonObjectArray {
    public static void main(String[] args) {
        JSONArray myArray = new JSONArray();

        for (String string : args) {
            JSONObject obj = new JSONObject();
            obj.put(string.toUpperCase(), string.length());
            myArray.add(obj);
        }

        System.out.println(myArray.toJSONString());
    }
}

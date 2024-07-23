// Script outputs arrays of objects as JSON

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class JsonObjectArray {
    public static void main(String[] args) throws Exception{
        if (args.length == 0) {
            System.out.println("Usage: java JsonObjectArray <string1> <string2> ...");
            System.exit(1);
        }

        ObjectMapper objectMapper = new ObjectMapper();
        ArrayNode arrayNode = objectMapper.createArrayNode();

        for (String string : args) {
            ObjectNode obj = objectMapper.createObjectNode();
            obj.put(string.toUpperCase(), string.length());
            arrayNode.add(obj);
        }

        String jsonArrayString = objectMapper.writeValueAsString(arrayNode);
        System.out.println(jsonArrayString);
    }
}

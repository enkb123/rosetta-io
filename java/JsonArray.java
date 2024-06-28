//Script takes args and turns into JSON array

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

public class JsonArray {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java JsonArray <string1> <string2> ...");
            System.exit(1);
        }

        ObjectMapper objectMapper = new ObjectMapper();
        ArrayNode arrayNode = objectMapper.createArrayNode();

        for (String arg : args) {
            arrayNode.add(arg);
        }

        String jsonArrayString = arrayNode.toString();

        System.out.println(jsonArrayString);
    }
}

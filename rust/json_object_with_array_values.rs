// Script takes arguments and transforms them into dict with arrays as dict values
// and returns as JSON

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.util.Arrays;

public class JsonObjectWithArrayValues {
    public static void main(String[] args) throws Exception{
        if (args.length == 0) {
            System.out.println("Usage: java JsonFromStrings <string1> <string2> ...");
            System.exit(1);
        }

        ObjectMapper objectMapper = new ObjectMapper();

        ObjectNode jsonObject = objectMapper.createObjectNode();

        Arrays.stream(args).forEach(str -> {
            ArrayNode lettersArray = objectMapper.createArrayNode();
            str.toUpperCase().chars().forEach(c -> lettersArray.add(String.valueOf((char) c)));
            jsonObject.set(str, lettersArray);
        });

        String jsonString = objectMapper.writeValueAsString(jsonObject);
        System.out.println(jsonString);
    }
}

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class JsonObjectWithArrayValues {
    public static void main(String[] args) throws Exception {
        var objectMapper = new ObjectMapper();

        var jsonObject = objectMapper.createObjectNode();

        for (String str : args) {
            var lettersArray = objectMapper.createArrayNode();
            str.toUpperCase().chars().forEach(c -> lettersArray.add(String.valueOf((char) c)));
            jsonObject.set(str, lettersArray);
        }

        String jsonString = objectMapper.writeValueAsString(jsonObject);
        System.out.println(jsonString);
    }
}

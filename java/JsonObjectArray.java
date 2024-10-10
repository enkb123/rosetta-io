import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

public class JsonObjectArray {
    public static void main(String[] args) throws Exception {
        var objectMapper = new ObjectMapper();
        var arrayNode = objectMapper.createArrayNode();

        for (String string : args) {
            var obj = objectMapper.createObjectNode();
            obj.put(string.toUpperCase(), string.length());
            arrayNode.add(obj);
        }

        String jsonArrayString = objectMapper.writeValueAsString(arrayNode);
        System.out.println(jsonArrayString);
    }
}

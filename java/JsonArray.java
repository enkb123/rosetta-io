import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

public class JsonArray {
    public static void main(String[] args) {
        var objectMapper = new ObjectMapper();
        var arrayNode = objectMapper.createArrayNode();

        for (String arg : args) {
            arrayNode.add(arg);
        }

        String jsonArrayString = arrayNode.toString();

        System.out.println(jsonArrayString);
    }
}

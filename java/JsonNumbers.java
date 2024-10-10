import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

public class JsonNumbers {
    public static void main(String[] args) throws Exception {
        var objectMapper = new ObjectMapper();
        var arrayNode = objectMapper.createArrayNode();

        for (String str : args) {
            arrayNode.add(str.length());
        }

        String jsonArrayString = objectMapper.writeValueAsString(arrayNode);
        System.out.println(jsonArrayString);
    }
}

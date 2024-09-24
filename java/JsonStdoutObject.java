import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class JsonStdoutObject {
    public static void main(String[] args) throws Exception{
        var objectMapper = new ObjectMapper();

        var jsonObject = objectMapper.createObjectNode();

        for (String string : args) {
            jsonObject.put(string, string.length());
        }

        var jsonString = objectMapper.writeValueAsString(jsonObject);
        System.out.println(jsonString);
    }
}

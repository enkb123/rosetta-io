//Script takes control characters and outputs valid JSON
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonControlChars {
    public static void main(String[] args) throws JsonProcessingException{
        if (args.length == 0) {
            System.out.println("Usage: java JsonControlChars <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        ObjectMapper objectMapper = new ObjectMapper();

        // Convert testString to JSON string
        String jsonString = objectMapper.writeValueAsString(testString);
        System.out.println(jsonString);

    }
}

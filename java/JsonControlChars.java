import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonControlChars {
    public static void main(String[] args) throws Exception {
        String testString = args[0];
        var objectMapper = new ObjectMapper();

        String jsonString = objectMapper.writeValueAsString(testString);
        System.out.println(jsonString);

    }
}

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.*;

public class JsonOutputtingData {

    public static void main(String[] args) throws Exception {
        var firstJsonObject = new HashMap<>(); // Can't use Map.of() because it doesn't support null values
        firstJsonObject.put("true", true);
        firstJsonObject.put("false", false);
        firstJsonObject.put("zero", 0);
        firstJsonObject.put("int", 42);
        firstJsonObject.put("float", 3.14);
        firstJsonObject.put("null", null);
        firstJsonObject.put("empty string", "");
        firstJsonObject.put("a string with non-ascii characters", "hello \n \0 \u0001 world 🥸");

        var secondJsonObject = Map.of(
            "array of strings", List.of("abc", "def", "ghi", "jkl"),
            "array of numbers", List.of(13, 42, 9000, -7),
            "array of nothing", List.of(),
            "array of mixed", Arrays.asList(13, "def", null, false, List.of("a"), Map.of("o", 1)),
            "array of objects", List.of(
                Map.of(
                    "name", "Bob Barker",
                    "age", 84
                ),
                Map.of(
                    "address1", "123 Main St",
                    "address2", "Apt 1"
                )
            ),
            "array of arrays", List.of(
                List.of("a", "b", "c"),
                List.of("d", "e", "f")
            )
        );

        var thirdJsonObject = Map.of(
            "objects", Map.of(
                "nested", Map.of(
                    "objects", Map.of(
                        "are", "supported"
                    )
                )
            )
        );

        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.SerializationFeature.INDENT_OUTPUT);
        printJson(objectMapper, firstJsonObject);
        printJson(objectMapper, secondJsonObject);
        printJson(objectMapper, thirdJsonObject);
    }

    private static void printJson(ObjectMapper objectMapper, Object data) throws JsonProcessingException {
        String jsonData = objectMapper.writeValueAsString(data);
        System.out.println(jsonData);
    }
}

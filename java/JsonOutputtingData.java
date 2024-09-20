import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.*;

public class JsonOutputtingData {

    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.SerializationFeature.INDENT_OUTPUT);

        Map<String, Object> firstJsonObject = new LinkedHashMap<>();
        firstJsonObject.put("true", true);
        firstJsonObject.put("false", false);
        firstJsonObject.put("zero", 0);
        firstJsonObject.put("int", 42);
        firstJsonObject.put("float", 3.14);
        firstJsonObject.put("null", null);
        firstJsonObject.put("empty string", "");
        firstJsonObject.put("a string with non-ascii characters", "hello \n \0 \u0001 world 🥸");

        Map<String, Object> secondJsonObject = new LinkedHashMap<>();
        secondJsonObject.put("array of strings", Arrays.asList("abc", "def", "ghi", "jkl"));
        secondJsonObject.put("array of numbers", Arrays.asList(13, 42, 9000, -7));
        secondJsonObject.put("array of nothing", new ArrayList<>());
        secondJsonObject.put("array of mixed", Arrays.asList(13, "def", null, false, Arrays.asList("a"), Collections.singletonMap("o", 1)));
        secondJsonObject.put("array of objects", Arrays.asList(
            new LinkedHashMap<String, Object>() {{ put("name", "Bob Barker"); put("age", 84); }},
            new LinkedHashMap<String, Object>() {{ put("address1", "123 Main St"); put("address2", "Apt 1"); }}
        ));
        secondJsonObject.put("array of arrays", Arrays.asList(
            Arrays.asList("a", "b", "c"),
            Arrays.asList("d", "e", "f")
        ));

        Map<String, Object> thirdJsonObject = new LinkedHashMap<>();
        thirdJsonObject.put("objects", Collections.singletonMap("nested", Collections.singletonMap("objects", Collections.singletonMap("are", "supported"))));

        printJson(objectMapper, firstJsonObject);
        printJson(objectMapper, secondJsonObject);
        printJson(objectMapper, thirdJsonObject);
    }

    private static void printJson(ObjectMapper objectMapper, Object data) throws JsonProcessingException {
        String jsonData = objectMapper.writeValueAsString(data);
        System.out.println(jsonData);
    }
}

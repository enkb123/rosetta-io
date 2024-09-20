import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;

public class ReadJsonFile {
    public static void main(String[] args) throws IOException{
        String filePath = "people.json";
        ObjectMapper objectMapper = new ObjectMapper();

        JsonNode people = objectMapper.readTree(new File(filePath));
        for (JsonNode person : people) {
            int age = person.get("age").asInt();
            String firstName = person.get("first_name").asText();
            System.out.printf("Hello, %d year old %s%n", age, firstName);
        }
    }
}

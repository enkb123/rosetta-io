import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;

public class ReadJsonFile {
    public static void main(String[] args) throws Exception {
        var file = new File("people.json");

        new ObjectMapper()
            .readTree(file)
            .elements()
            .forEachRemaining(person -> {
                var age = person.get("age").asInt();
                var firstName = person.get("first_name").asText();

                System.out.printf("Hello, %d year old %s%n", age, firstName);
            });
        }
    }

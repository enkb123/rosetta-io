// Read JSON file, transform and print to stdout
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class ReadJsonFile {
    public static void main(String[] args) throws IOException{
        if (args.length < 1) {
            System.out.println("Usage: java ReadJsonFile <json_file>");
            return;
        }
        JsonNode people = new ObjectMapper().readTree(new File(args[0]));
        people.forEach(person -> System.out.println("Hello, " + person.get("age").asLong() + " year old " + person.get("first_name").asText()));

    }
}

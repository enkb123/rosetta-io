// Read JSON file, transform and print to stdout
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import java.io.FileReader;

public class ReadJsonFile {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java ReadJsonFile.java <json_file>");
            return;
        }

        String jsonFile = args[0];

        JSONParser parser = new JSONParser();

        try {
            JSONArray people = (JSONArray) parser.parse(new FileReader(jsonFile));

            for (Object obj : people) {
                JSONObject person = (JSONObject) obj;
                long age = (long) person.get("age");
                String firstName = (String) person.get("first_name");
                System.out.println("Hello, " + age + " year old " + firstName);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// Script takes string arguments and outputs a JSON array of numbers representing
// the length of each argument
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

public class JsonNumbers {
    public static void main(String[] args) throws Exception{
        if (args.length == 0) {
            System.out.println("Usage: java JsonNumbers <string1> <string2> ...");
            System.exit(1);
        }

        ArrayNode arrayNode = new ObjectMapper().createArrayNode();

        for (String str : args) {
            arrayNode.add(str.length());
        }

        String jsonArrayString = new ObjectMapper().writeValueAsString(arrayNode);
        System.out.println(jsonArrayString);
    }
}


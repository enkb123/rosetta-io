import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonNullChar {
    public static void main(String[] args) throws Exception {
        var str = "Hello World \0";
        var jsonData = new ObjectMapper().writeValueAsString(str);
        System.out.println(jsonData);
    }
}

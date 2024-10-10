import java.util.Base64;

public class Encode {
    public static void main(String[] args) {
        String testString = args[0];
        String encodedString = Base64.getEncoder().encodeToString(testString.getBytes());

        System.out.println(encodedString);
    }
}

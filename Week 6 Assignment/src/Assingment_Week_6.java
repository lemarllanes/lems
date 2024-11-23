import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Assingment_Week_6 {
    public static void main(String[] args) {
        // Hardcoded credentials (security risk)
        String dbUrl = "jdbc:mysql://localhost:3306/testdb";
        String username = "root";
        String password = "password";

        // Unused variable
        int unusedVariable = 10;

        try {
            Connection connection = DriverManager.getConnection(dbUrl, username, password);
            Statement statement = connection.createStatement();

            // SQL injection vulnerability
            String userInput = "1 OR 1=1"; // Simulated malicious input
            String query = "SELECT * FROM users WHERE id = " + userInput;
            ResultSet resultSet = statement.executeQuery(query);

            while (resultSet.next()) {
                System.out.println("User: " + resultSet.getString("name"));
            }

        } catch (Exception e) {
            // Poor error handling
            e.printStackTrace();
        }
    }
}

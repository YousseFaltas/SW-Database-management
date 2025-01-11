import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class DatabaseConnection {

    // Method to establish and return a database connection
    public static Connection getConnection() throws SQLException {
        String url = "jdbc:sqlserver://DESKTOP-2354QUB\\SQLEXPRESS:1433;databaseName=Faith;integratedSecurity=true;encrypt=true;trustServerCertificate=true";
        String username = "your_sql_server_username"; // Replace with your SQL Server username
        String password = "your_sql_server_password"; // Replace with your SQL Server password

        // Establish the connection and return it
        return DriverManager.getConnection(url, username, password);
    }

    // Method to fetch hotel data from the database
    public static List<Hotels> fetchHotels() {
        List<Hotels> hotelsList = new ArrayList<>();

        try (Connection conn = getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM Hotel")) {

            // Map ResultSet to Hotels objects
            while (rs.next()) {
                int hotelID = rs.getInt("H_id");
                String name = rs.getString("H_name");
                String location = rs.getString("H_loc");
                String policy = rs.getString("H_policy");
                String email = rs.getString("H_email");
                String phoneNumber = rs.getString("H_phone");
                String website = rs.getString("H_website");

                Hotels hotel = new Hotels(hotelID, name, location, policy, email, phoneNumber, website);
                hotelsList.add(hotel);
            }

        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
        }

        return hotelsList;
    }

    // Main method for testing the connection and displaying hotel data
    public static void main(String[] args) {
        try {
            // Test the connection
            Connection conn = DatabaseConnection.getConnection();
            System.out.println("Connection to SQL Server successful!");

            // Fetch and display hotel data
            List<Hotels> hotelsList = fetchHotels();
            System.out.println("\nHotel Information:");
            System.out.println("==================");
            for (Hotels hotel : hotelsList) {
                System.out.println(hotel); // Calls the toString() method
                System.out.println("------------------");
            }

            // Close the connection when done
            conn.close();
        } catch (SQLException e) {
            System.err.println("Connection failed: " + e.getMessage());
        }
    }
}
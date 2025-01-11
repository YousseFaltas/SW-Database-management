import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Airline {

    // Declare the fields with appropriate data types
    private int Air_ID;
    private String Air_Name;
    private String Air_Policy;
    private String Air_Email;
    private String Air_PhoneNum;
    private String Air_Website;

    // Default constructor
    public Airline() {
    }

    // Parameterized constructor
    public Airline(int Air_ID, String Air_Name, String Air_Policy, String Air_Email, String Air_PhoneNum, String Air_Website) {
        this.Air_ID = Air_ID;
        this.Air_Name = Air_Name;
        this.Air_Policy = Air_Policy;
        this.Air_Email = Air_Email;
        this.Air_PhoneNum = Air_PhoneNum;
        this.Air_Website = Air_Website;
    }

    // Getter and Setter methods
    public int getAir_ID() {
        return Air_ID;
    }

    public void setAir_ID(int Air_ID) {
        this.Air_ID = Air_ID;
    }

    public String getAir_Name() {
        return Air_Name;
    }

    public void setAir_Name(String Air_Name) {
        this.Air_Name = Air_Name;
    }

    public String getAir_Policy() {
        return Air_Policy;
    }

    public void setAir_Policy(String Air_Policy) {
        this.Air_Policy = Air_Policy;
    }

    public String getAir_Email() {
        return Air_Email;
    }

    public void setAir_Email(String Air_Email) {
        this.Air_Email = Air_Email;
    }

    public String getAir_PhoneNum() {
        return Air_PhoneNum;
    }

    public void setAir_PhoneNum(String Air_PhoneNum) {
        this.Air_PhoneNum = Air_PhoneNum;
    }

    public String getAir_Website() {
        return Air_Website;
    }

    public void setAir_Website(String Air_Website) {
        this.Air_Website = Air_Website;
    }

    // CRUD methods

    // Save (Insert) airline into the database
    public void save(Connection conn) throws SQLException {
        String query = "INSERT INTO dbo.airline (Air_ID, Air_Name, Air_Policy, Air_Email, Air_PhoneNum, Air_Website) VALUES (?, ?, ?, ?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, this.Air_ID);
            stmt.setString(2, this.Air_Name);
            stmt.setString(3, this.Air_Policy);
            stmt.setString(4, this.Air_Email);
            stmt.setString(5, this.Air_PhoneNum);
            stmt.setString(6, this.Air_Website);
            stmt.executeUpdate();
        }
    }

    // Get airline by ID (Read)
    public static Airline getById(Connection conn, int id) throws SQLException {
        String query = "SELECT * FROM dbo.airline WHERE Air_ID = ?";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return new Airline(
                        rs.getInt("Air_ID"),
                        rs.getString("Air_Name"),
                        rs.getString("Air_Policy"),
                        rs.getString("Air_Email"),
                        rs.getString("Air_PhoneNum"),
                        rs.getString("Air_Website")
                );
            } else {
                return null;
            }
        }
    }

    // Update airline details in the database
    public void update(Connection conn) throws SQLException {
        String query = "UPDATE dbo.airline SET Air_Name = ?, Air_Policy = ?, Air_Email = ?, Air_PhoneNum = ?, Air_Website = ? WHERE Air_ID = ?";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, this.Air_Name);
            stmt.setString(2, this.Air_Policy);
            stmt.setString(3, this.Air_Email);
            stmt.setString(4, this.Air_PhoneNum);
            stmt.setString(5, this.Air_Website);
            stmt.setInt(6, this.Air_ID);
            stmt.executeUpdate();
        }
    }

    // Delete airline from the database
    public void delete(Connection conn) throws SQLException {
        String query = "DELETE FROM dbo.airline WHERE Air_ID = ?";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, this.Air_ID);
            stmt.executeUpdate();
        }
    }
}

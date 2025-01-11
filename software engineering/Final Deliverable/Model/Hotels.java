import java.io.Serializable;

public class Hotels implements Serializable {
    private int hotelID;
    private String name;
    private String location;
    private String policy;
    private String email;
    private String phoneNumber;
    private String website;

    // Default constructor
    public Hotels() {}

    // Parameterized constructor
    public Hotels(int hotelID, String name, String location, String policy,
                  String email, String phoneNumber, String website) {
        this.hotelID = hotelID;
        this.name = name;
        this.location = location;
        this.policy = policy;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.website = website;
    }

    // Getters and setters
    public int getHotelID() {
        return hotelID;
    }

    public void setHotelID(int hotelID) {
        this.hotelID = hotelID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getPolicy() {
        return policy;
    }

    public void setPolicy(String policy) {
        this.policy = policy;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "Hotels{" +
                "hotelID=" + hotelID +
                ", name='" + name + '\'' +
                ", location='" + location + '\'' +
                ", policy='" + policy + '\'' +
                ", email='" + email + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", website='" + website + '\'' +
                '}';
    }
}

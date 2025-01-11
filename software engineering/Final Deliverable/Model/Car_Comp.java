import java.io.Serializable;

public class Car_Comp implements Serializable {
    private int compID;
    private String compName;
    private String pickupLocation;
    private String dropOffLocation;
    private String compPolicy;
    private String compEmail;
    private String compPhoneNumber;
    private String compWebsite;

    // Default constructor
    public Car_Comp() {}

    // Parameterized constructor
    public Car_Comp(int compID, String compName, String pickupLocation, String dropOffLocation,
                    String compPolicy, String compEmail, String compPhoneNumber, String compWebsite) {
        this.compID = compID;
        this.compName = compName;
        this.pickupLocation = pickupLocation;
        this.dropOffLocation = dropOffLocation;
        this.compPolicy = compPolicy;
        this.compEmail = compEmail;
        this.compPhoneNumber = compPhoneNumber;
        this.compWebsite = compWebsite;
    }

    // Getters and setters
    public int getCompID() {
        return compID;
    }

    public void setCompID(int compID) {
        this.compID = compID;
    }

    public String getCompName() {
        return compName;
    }

    public void setCompName(String compName) {
        this.compName = compName;
    }

    public String getPickupLocation() {
        return pickupLocation;
    }

    public void setPickupLocation(String pickupLocation) {
        this.pickupLocation = pickupLocation;
    }

    public String getDropOffLocation() {
        return dropOffLocation;
    }

    public void setDropOffLocation(String dropOffLocation) {
        this.dropOffLocation = dropOffLocation;
    }

    public String getCompPolicy() {
        return compPolicy;
    }

    public void setCompPolicy(String compPolicy) {
        this.compPolicy = compPolicy;
    }

    public String getCompEmail() {
        return compEmail;
    }

    public void setCompEmail(String compEmail) {
        this.compEmail = compEmail;
    }

    public String getCompPhoneNumber() {
        return compPhoneNumber;
    }

    public void setCompPhoneNumber(String compPhoneNumber) {
        this.compPhoneNumber = compPhoneNumber;
    }

    public String getCompWebsite() {
        return compWebsite;
    }

    public void setCompWebsite(String compWebsite) {
        this.compWebsite = compWebsite;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "Car_Comp{" +
                "compID=" + compID +
                ", compName='" + compName + '\'' +
                ", pickupLocation='" + pickupLocation + '\'' +
                ", dropOffLocation='" + dropOffLocation + '\'' +
                ", compPolicy='" + compPolicy + '\'' +
                ", compEmail='" + compEmail + '\'' +
                ", compPhoneNumber='" + compPhoneNumber + '\'' +
                ", compWebsite='" + compWebsite + '\'' +
                '}';
    }
}

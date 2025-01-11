import java.io.Serializable;

public class Room implements Serializable {
    private int roomID;
    private int roomNumber;
    private String roomType;
    private double roomPrice;
    private boolean roomAvailability;
    private String roomAmenities;

    // Default constructor
    public Room() {}

    // Parameterized constructor
    public Room(int roomID, int roomNumber, String roomType, double roomPrice, boolean roomAvailability, String roomAmenities) {
        this.roomID = roomID;
        this.roomNumber = roomNumber;
        this.roomType = roomType;
        this.roomPrice = roomPrice;
        this.roomAvailability = roomAvailability;
        this.roomAmenities = roomAmenities;
    }

    // Getters and setters
    public int getRoomID() {
        return roomID;
    }

    public void setRoomID(int roomID) {
        this.roomID = roomID;
    }

    public int getRoomNumber() {
        return roomNumber;
    }

    public void setRoomNumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }

    public String getRoomType() {
        return roomType;
    }

    public void setRoomType(String roomType) {
        this.roomType = roomType;
    }

    public double getRoomPrice() {
        return roomPrice;
    }

    public void setRoomPrice(double roomPrice) {
        this.roomPrice = roomPrice;
    }

    public boolean isRoomAvailability() {
        return roomAvailability;
    }

    public void setRoomAvailability(boolean roomAvailability) {
        this.roomAvailability = roomAvailability;
    }

    public String getRoomAmenities() {
        return roomAmenities;
    }

    public void setRoomAmenities(String roomAmenities) {
        this.roomAmenities = roomAmenities;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "Room{" +
                "roomID=" + roomID +
                ", roomNumber=" + roomNumber +
                ", roomType='" + roomType + '\'' +
                ", roomPrice=" + roomPrice +
                ", roomAvailability=" + roomAvailability +
                ", roomAmenities='" + roomAmenities + '\'' +
                '}';
    }
}

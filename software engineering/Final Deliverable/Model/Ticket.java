import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalTime;

public class Ticket implements Serializable {
    private int ticketID;
    private String flightNo;
    private String departureLocation;
    private LocalDate departureDate;
    private LocalTime departureTime;
    private String arrivalLocation;
    private LocalDate arrivalDate;
    private LocalTime arrivalTime;
    private String seatNo;
    private String seatDescription;
    private String ticketClass; // Renamed "class" to "ticketClass" (reserved keyword issue)
    private double price;

    // Default constructor
    public Ticket() {}

    // Parameterized constructor
    public Ticket(int ticketID, String flightNo, String departureLocation, LocalDate departureDate,
                  LocalTime departureTime, String arrivalLocation, LocalDate arrivalDate,
                  LocalTime arrivalTime, String seatNo, String seatDescription, String ticketClass, double price) {
        this.ticketID = ticketID;
        this.flightNo = flightNo;
        this.departureLocation = departureLocation;
        this.departureDate = departureDate;
        this.departureTime = departureTime;
        this.arrivalLocation = arrivalLocation;
        this.arrivalDate = arrivalDate;
        this.arrivalTime = arrivalTime;
        this.seatNo = seatNo;
        this.seatDescription = seatDescription;
        this.ticketClass = ticketClass;
        this.price = price;
    }

    // Getters and setters
    public int getTicketID() {
        return ticketID;
    }

    public void setTicketID(int ticketID) {
        this.ticketID = ticketID;
    }

    public String getFlightNo() {
        return flightNo;
    }

    public void setFlightNo(String flightNo) {
        this.flightNo = flightNo;
    }

    public String getDepartureLocation() {
        return departureLocation;
    }

    public void setDepartureLocation(String departureLocation) {
        this.departureLocation = departureLocation;
    }

    public LocalDate getDepartureDate() {
        return departureDate;
    }

    public void setDepartureDate(LocalDate departureDate) {
        this.departureDate = departureDate;
    }

    public LocalTime getDepartureTime() {
        return departureTime;
    }

    public void setDepartureTime(LocalTime departureTime) {
        this.departureTime = departureTime;
    }

    public String getArrivalLocation() {
        return arrivalLocation;
    }

    public void setArrivalLocation(String arrivalLocation) {
        this.arrivalLocation = arrivalLocation;
    }

    public LocalDate getArrivalDate() {
        return arrivalDate;
    }

    public void setArrivalDate(LocalDate arrivalDate) {
        this.arrivalDate = arrivalDate;
    }

    public LocalTime getArrivalTime() {
        return arrivalTime;
    }

    public void setArrivalTime(LocalTime arrivalTime) {
        this.arrivalTime = arrivalTime;
    }

    public String getSeatNo() {
        return seatNo;
    }

    public void setSeatNo(String seatNo) {
        this.seatNo = seatNo;
    }

    public String getSeatDescription() {
        return seatDescription;
    }

    public void setSeatDescription(String seatDescription) {
        this.seatDescription = seatDescription;
    }

    public String getTicketClass() {
        return ticketClass;
    }

    public void setTicketClass(String ticketClass) {
        this.ticketClass = ticketClass;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "Ticket{" +
                "ticketID=" + ticketID +
                ", flightNo='" + flightNo + '\'' +
                ", departureLocation='" + departureLocation + '\'' +
                ", departureDate=" + departureDate +
                ", departureTime=" + departureTime +
                ", arrivalLocation='" + arrivalLocation + '\'' +
                ", arrivalDate=" + arrivalDate +
                ", arrivalTime=" + arrivalTime +
                ", seatNo='" + seatNo + '\'' +
                ", seatDescription='" + seatDescription + '\'' +
                ", ticketClass='" + ticketClass + '\'' +
                ", price=" + price +
                '}';
    }
}

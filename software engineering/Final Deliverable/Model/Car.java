import java.io.Serializable;

public class Car implements Serializable {
    private int carID;
    private String licenseNum;
    private String model;
    private String make;
    private String carType;
    private int year;
    private String transmissionType;
    private int numSeats;
    private String features;
    private String fuelType;
    private double rentalPrice;

    // Default constructor
    public Car() {}

    // Parameterized constructor
    public Car(int carID, String licenseNum, String model, String make, String carType, int year,
               String transmissionType, int numSeats, String features, String fuelType, double rentalPrice) {
        this.carID = carID;
        this.licenseNum = licenseNum;
        this.model = model;
        this.make = make;
        this.carType = carType;
        this.year = year;
        this.transmissionType = transmissionType;
        this.numSeats = numSeats;
        this.features = features;
        this.fuelType = fuelType;
        this.rentalPrice = rentalPrice;
    }

    // Getters and setters
    public int getCarID() {
        return carID;
    }

    public void setCarID(int carID) {
        this.carID = carID;
    }

    public String getLicenseNum() {
        return licenseNum;
    }

    public void setLicenseNum(String licenseNum) {
        this.licenseNum = licenseNum;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getMake() {
        return make;
    }

    public void setMake(String make) {
        this.make = make;
    }

    public String getCarType() {
        return carType;
    }

    public void setCarType(String carType) {
        this.carType = carType;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getTransmissionType() {
        return transmissionType;
    }

    public void setTransmissionType(String transmissionType) {
        this.transmissionType = transmissionType;
    }

    public int getNumSeats() {
        return numSeats;
    }

    public void setNumSeats(int numSeats) {
        this.numSeats = numSeats;
    }

    public String getFeatures() {
        return features;
    }

    public void setFeatures(String features) {
        this.features = features;
    }

    public String getFuelType() {
        return fuelType;
    }

    public void setFuelType(String fuelType) {
        this.fuelType = fuelType;
    }

    public double getRentalPrice() {
        return rentalPrice;
    }

    public void setRentalPrice(double rentalPrice) {
        this.rentalPrice = rentalPrice;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "Car{" +
                "carID=" + carID +
                ", licenseNum='" + licenseNum + '\'' +
                ", model='" + model + '\'' +
                ", make='" + make + '\'' +
                ", carType='" + carType + '\'' +
                ", year=" + year +
                ", transmissionType='" + transmissionType + '\'' +
                ", numSeats=" + numSeats +
                ", features='" + features + '\'' +
                ", fuelType='" + fuelType + '\'' +
                ", rentalPrice=" + rentalPrice +
                '}';
    }
}

import java.io.Serializable;
import java.time.LocalDate;

public class UserProfile implements Serializable {
    private int customerId;
    private String customerName;
    private String customerPhoneNumber;
    private String customerEmail;
    private String customerAddress;
    private String nationality;
    private String bankAccount;
    private LocalDate dateOfBirth;
    private boolean creditWorthiness;

    // Default constructor
    public UserProfile() {}

    // Parameterized constructor
    public UserProfile(int customerId, String customerName, String customerPhoneNumber, String customerEmail,
                       String customerAddress, String nationality, String bankAccount,
                       LocalDate dateOfBirth, boolean creditWorthiness) {
        this.customerId = customerId;
        this.customerName = customerName;
        this.customerPhoneNumber = customerPhoneNumber;
        this.customerEmail = customerEmail;
        this.customerAddress = customerAddress;
        this.nationality = nationality;
        this.bankAccount = bankAccount;
        this.dateOfBirth = dateOfBirth;
        this.creditWorthiness = creditWorthiness;
    }

    // Getters and setters
    public int getCustomerId() {
        return customerId;
    }

    public void setCustomerId(int customerId) {
        this.customerId = customerId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getCustomerPhoneNumber() {
        return customerPhoneNumber;
    }

    public void setCustomerPhoneNumber(String customerPhoneNumber) {
        this.customerPhoneNumber = customerPhoneNumber;
    }

    public String getCustomerEmail() {
        return customerEmail;
    }

    public void setCustomerEmail(String customerEmail) {
        this.customerEmail = customerEmail;
    }

    public String getCustomerAddress() {
        return customerAddress;
    }

    public void setCustomerAddress(String customerAddress) {
        this.customerAddress = customerAddress;
    }

    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }

    public String getBankAccount() {
        return bankAccount;
    }

    public void setBankAccount(String bankAccount) {
        this.bankAccount = bankAccount;
    }

    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public boolean isCreditWorthiness() {
        return creditWorthiness;
    }

    public void setCreditWorthiness(boolean creditWorthiness) {
        this.creditWorthiness = creditWorthiness;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "UserProfile{" +
                "customerId=" + customerId +
                ", customerName='" + customerName + '\'' +
                ", customerPhoneNumber='" + customerPhoneNumber + '\'' +
                ", customerEmail='" + customerEmail + '\'' +
                ", customerAddress='" + customerAddress + '\'' +
                ", nationality='" + nationality + '\'' +
                ", bankAccount='" + bankAccount + '\'' +
                ", dateOfBirth=" + dateOfBirth +
                ", creditWorthiness=" + creditWorthiness +
                '}';
    }
}

import java.io.Serializable;
import java.util.Date;

public class Order implements Serializable {
    private int orderID;
    private String bookingStatus;
    private String products;
    private String salesDepartmentEmployee;
    private String customerPreferences;
    private Date orderDate;
    private String orderApplication;
    private String salesDeptDigitalSignature;

    // Default constructor
    public Order() {}

    // Parameterized constructor
    public Order(int orderID, String bookingStatus, String products, String salesDepartmentEmployee,
                 String customerPreferences, Date orderDate, String orderApplication,
                 String salesDeptDigitalSignature) {
        this.orderID = orderID;
        this.bookingStatus = bookingStatus;
        this.products = products;
        this.salesDepartmentEmployee = salesDepartmentEmployee;
        this.customerPreferences = customerPreferences;
        this.orderDate = orderDate;
        this.orderApplication = orderApplication;
        this.salesDeptDigitalSignature = salesDeptDigitalSignature;
    }

    // Getters and setters
    public int getOrderID() {
        return orderID;
    }

    public void setOrderID(int orderID) {
        this.orderID = orderID;
    }

    public String getBookingStatus() {
        return bookingStatus;
    }

    public void setBookingStatus(String bookingStatus) {
        this.bookingStatus = bookingStatus;
    }

    public String getProducts() {
        return products;
    }

    public void setProducts(String products) {
        this.products = products;
    }

    public String getSalesDepartmentEmployee() {
        return salesDepartmentEmployee;
    }

    public void setSalesDepartmentEmployee(String salesDepartmentEmployee) {
        this.salesDepartmentEmployee = salesDepartmentEmployee;
    }

    public String getCustomerPreferences() {
        return customerPreferences;
    }

    public void setCustomerPreferences(String customerPreferences) {
        this.customerPreferences = customerPreferences;
    }

    public Date getOrderDate() {
        return orderDate;
    }

    public void setOrderDate(Date orderDate) {
        this.orderDate = orderDate;
    }

    public String getOrderApplication() {
        return orderApplication;
    }

    public void setOrderApplication(String orderApplication) {
        this.orderApplication = orderApplication;
    }

    public String getSalesDeptDigitalSignature() {
        return salesDeptDigitalSignature;
    }

    public void setSalesDeptDigitalSignature(String salesDeptDigitalSignature) {
        this.salesDeptDigitalSignature = salesDeptDigitalSignature;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "Order{" +
                "orderID=" + orderID +
                ", bookingStatus='" + bookingStatus + '\'' +
                ", products='" + products + '\'' +
                ", salesDepartmentEmployee='" + salesDepartmentEmployee + '\'' +
                ", customerPreferences='" + customerPreferences + '\'' +
                ", orderDate=" + orderDate +
                ", orderApplication='" + orderApplication + '\'' +
                ", salesDeptDigitalSignature='" + salesDeptDigitalSignature + '\'' +
                '}';
    }
}

import java.io.Serializable;

public class Payment implements Serializable {
    private int payRefNum;
    private double paidAmount;
    private String status;
    private double discount;
    private String cancellationReturnPolicy;

    // Default constructor
    public Payment() {}

    // Parameterized constructor
    public Payment(int payRefNum, double paidAmount, String status, double discount, String cancellationReturnPolicy) {
        this.payRefNum = payRefNum;
        this.paidAmount = paidAmount;
        this.status = status;
        this.discount = discount;
        this.cancellationReturnPolicy = cancellationReturnPolicy;
    }

    // Getters and setters
    public int getPayRefNum() {
        return payRefNum;
    }

    public void setPayRefNum(int payRefNum) {
        this.payRefNum = payRefNum;
    }

    public double getPaidAmount() {
        return paidAmount;
    }

    public void setPaidAmount(double paidAmount) {
        this.paidAmount = paidAmount;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public double getDiscount() {
        return discount;
    }

    public void setDiscount(double discount) {
        this.discount = discount;
    }

    public String getCancellationReturnPolicy() {
        return cancellationReturnPolicy;
    }

    public void setCancellationReturnPolicy(String cancellationReturnPolicy) {
        this.cancellationReturnPolicy = cancellationReturnPolicy;
    }

    // Override toString for debugging and display
    @Override
    public String toString() {
        return "Payment{" +
                "payRefNum=" + payRefNum +
                ", paidAmount=" + paidAmount +
                ", status='" + status + '\'' +
                ", discount=" + discount +
                ", cancellationReturnPolicy='" + cancellationReturnPolicy + '\'' +
                '}';
    }
}

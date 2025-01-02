CREATE TABLE Room_booked (
Ord_id INT,
Cust_id INT,
H_id INT,
R_ID INT,
PRIMARY KEY (Ord_id , Cust_id , R_id, H_id ),
FOREIGN KEY (Ord_id) REFERENCES Orders(Ord_id),
FOREIGN KEY (Cust_id) REFERENCES Customer(Cust_id),
FOREIGN KEY (H_id,R_id) REFERENCES Room(H_id,R_id),
)

CREATE TABLE Car_rented(
Ord_id INT,
Cust_id INT,
Comp_id INT,
Car_id INT,
PRIMARY KEY (Ord_id , Cust_id , Comp_id , Car_id),
FOREIGN KEY (Ord_id) REFERENCES Orders(Ord_id),
FOREIGN KEY (Cust_id) REFERENCES Customer (Cust_id),
FOREIGN KEY (Comp_id,Car_id) REFERENCES Car(Comp_id , C_id)
)

CREATE TABLE Ticket_reserved(
Ord_id INT,
Cust_id INT,
Air_id INT,
Ticket_id INT,
PRIMARY KEY (Ord_id , Cust_id , Air_id , Ticket_id),
FOREIGN KEY (Ord_id) REFERENCES Orders(Ord_id),
FOREIGN KEY (Cust_id) REFERENCES Customer (Cust_id),
FOREIGN KEY (Air_id,Ticket_id) REFERENCES Ticket(Air_id , Ticket_id)
)
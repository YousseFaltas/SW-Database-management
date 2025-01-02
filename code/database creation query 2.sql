CREATE TABLE Orders(
Ord_id INT PRIMARY KEY,
Booking_status VARCHAR(30),
Products TEXT,
SalesDept_empl VARCHAR (100),
Cust_pref TEXT,
Ord_date DATE,
Ord_app VARBINARY(MAX),
Cust_id INT,
FOREIGN KEY (Cust_id) REFERENCES Customer(Cust_id)
)

CREATE TABLE Room (
R_id INT,
H_id INT,
R_num INT NOT NULL,
R_Type VARCHAR(50),
R_Price DECIMAL(10, 2) NOT NULL,
R_available VARCHAR(30) NOT NULL,
R_ameneties TEXT,
PRIMARY KEY(H_id,R_id),
FOREIGN KEY(H_id) REFERENCES Hotel(H_id)
)

CREATE TABLE Ticket(
Ticket_id INT,
Air_id INT,
flight_num VARCHAR(15) NOT NULL,
seat_num VARCHAR(15) NOT NULL,
dept_loc VARCHAR(50),
Arr_loc VARCHAR(50),
Dept_Time TIME,
Arr_Time TIME,
Dept_date DATE,
Arr_date DATE,
Class VARCHAR(30),
Ticket_Price DECIMAL(10, 2) NOT NULL,
Ticket_available VARCHAR(30) NOT NULL,
PRIMARY KEY(Ticket_id , Air_id),
FOREIGN KEY (Air_id) REFERENCES Airline(Air_id)
)

CREATE TABLE Car (
C_id INT,
Comp_id INT,
License_num VARCHAR(15) NOT NULL,
Model VARCHAR(30) NOT NULL,
Make VARCHAR(30) NOT NULL,
C_Type VARCHAR(30) NOT NULL,
C_year DATE NOT NULL,
Trans_Type VARCHAR(30),
Num_seats INT,
Features TEXT,
Fuel_Type VARCHAR(30),
Rental_price DECIMAL(10,2),
PRIMARY KEY (C_id, Comp_id),
FOREIGN KEY (Comp_id) REFERENCES Car_Comp(Comp_id)
)

CREATE TABLE Payment(
Pay_refnum INT,
Ord_id INT,
Paid_Amount DECIMAL (10,2),
Status VARCHAR(30),
Discount DECIMAL (10,2),
Conditions TEXT
PRIMARY KEY (Pay_refnum , Ord_id)
FOREIGN KEY (Ord_id) REFERENCES Orders(Ord_id)
)

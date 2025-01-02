
CREATE TABLE Airline(
Air_id INT PRIMARY KEY,
Air_name VARCHAR(100) NOT NULL,
Air_policy TEXT,
Air_email VARCHAR(100) UNIQUE,
Air_website VARCHAR(100),
Aie_phone VARCHAR(15)
)

CREATE TABLE Car_Comp (
Comp_id INT PRIMARY KEY,
Comp_name VARCHAR(100) NOT NULL,
Comp_policy TEXT,
Comp_email VARCHAR(100) UNIQUE,
Pickup_loc varchar(100) NOT NULL,
Dropoff_loc VARCHAR(100) NOT NULL,
Comp_website VARCHAR(100),
Comp_phone VARCHAR(15)
)

CREATE TABLE Customer (
Cust_id INT PRIMARY KEY,
Cust_name VARCHAR(100) NOT NULL,
Cust_email VARCHAR(100) UNIQUE,
Cust_phone VARCHAR(15),
Cust_address VARCHAR(255),
Nationality VARCHAR(50),
Bank_acc VARCHAR (20),
Date_birth DATE,
Credit_worthiness VARCHAR(30)
)

CREATE TABLE Hotel (
H_id INT PRIMARY KEY,
H_name VARCHAR(100) NOT NULL,
H_loc VARCHAR(100) NOT NULL,
H_policy TEXT,
H_email VARCHAR(100) UNIQUE,
H_phone VARCHAR(15),
H_website VARCHAR(100)
)


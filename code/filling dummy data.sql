-- Hotel Table
INSERT INTO Hotel (hotelID, hotelName, H_Loc, H_Policy, H_Email, H_PhoneNum, H_Website) VALUES
(1, 'The Ritz-Carlton', 'Cairo', 'No pets allowed', 'contact@ritzcairo.com', '01000000001', 'www.ritzcairo.com'),
(2, 'Hilton Alexandria', 'Alexandria', 'No smoking allowed', 'alexandria@hilton.com', '01000000002', 'www.hilton.com'),
(3, 'Four Seasons Resort', 'Sharm El-Sheikh', 'Pet-friendly', 'info@fourseasons.com', '01000000003', 'www.fourseasons.com'),
(4, 'Le Meridien', 'Luxor', 'Free Wi-Fi', 'luxor@lemeridien.com', '01000000004', 'www.lemeridien.com'),
(5, 'JW Marriott Cairo', 'Cairo', 'No parties allowed', 'jwmarriott@cairo.com', '01000000005', 'www.jwmarriott.com'),
(6, 'Sheraton Sharm', 'Sharm El-Sheikh', 'Quiet hours after 10pm', 'contact@sheratonsharm.com', '01000000006', 'www.sheraton.com'),
(7, 'Mena House', 'Giza', 'No loud music', 'mena@house.com', '01000000007', 'www.menahouse.com'),
(8, 'Radisson Blu', 'Cairo', 'No smoking in rooms', 'info@radissonblu.com', '01000000008', 'www.radissonblu.com'),
(9, 'St. Regis', 'Marsa Alam', 'Family-friendly', 'contact@stregismarsaalam.com', '01000000009', 'www.stregis.com'),
(10, 'Marriott Beach Resort', 'Hurghada', 'All-inclusive', 'hurghada@marriott.com', '01000000010', 'www.marriott.com');

-- Airline Table
INSERT INTO Airline (Air_ID, Air_Name, Air_Policy, Air_Email, Air_PhoneNum, Air_Website) VALUES
(1, 'EgyptAir', 'No pets allowed', 'info@egyptair.com', '1900', 'www.egyptair.com'),
(2, 'Emirates', 'No smoking in flight', 'contact@emirates.com', '1901', 'www.emirates.com'),
(3, 'Qatar Airways', 'Special assistance available', 'support@qatarairways.com', '1902', 'www.qatarairways.com'),
(4, 'Lufthansa', 'Food preference options', 'info@lufthansa.com', '1903', 'www.lufthansa.com'),
(5, 'British Airways', 'No alcohol served to minors', 'contact@britishairways.com', '1904', 'www.britishairways.com'),
(6, 'Air France', 'Free baggage allowance', 'help@airfrance.com', '1905', 'www.airfrance.com'),
(7, 'Turkish Airlines', 'No seat reservations for infants', 'support@turkishairlines.com', '1906', 'www.turkishairlines.com'),
(8, 'Delta Airlines', 'One free checked bag', 'info@delta.com', '1907', 'www.delta.com'),
(9, 'United Airlines', 'Online check-in only', 'help@united.com', '1908', 'www.united.com'),
(10, 'American Airlines', 'Pre-flight meal options', 'support@aa.com', '1909', 'www.aa.com');

-- Flight Table
INSERT INTO Flight (F_ID, F_Num, Dept_Loc, Dept_Date, Dept_Time, Arr_Loc, Arr_Date, Arr_Time, Air_ID) VALUES
(1, 'MSX123', 'Cairo', '2024-11-01', '08:00', 'New York', '2024-11-01', '14:00', 1),
(2, 'BA110', 'London', '2024-11-02', '10:00', 'Cairo', '2024-11-02', '16:00', 5),
(3, 'EK402', 'Dubai', '2024-11-03', '12:00', 'Sharm El-Sheikh', '2024-11-03', '15:00', 2),
(4, 'QR808', 'Doha', '2024-11-04', '09:00', 'Cairo', '2024-11-04', '13:00', 3),
(5, 'LH314', 'Frankfurt', '2024-11-05', '11:00', 'Sharm El-Sheikh', '2024-11-05', '15:30', 4),
(6, 'AF122', 'Paris', '2024-11-06', '13:00', 'Luxor', '2024-11-06', '17:30', 6),
(7, 'TK788', 'Istanbul', '2024-11-07', '10:00', 'Hurghada', '2024-11-07', '13:30', 7),
(8, 'DL201', 'Atlanta', '2024-11-08', '14:00', 'Cairo', '2024-11-08', '19:00', 8),
(9, 'UA460', 'Chicago', '2024-11-09', '16:00', 'New York', '2024-11-09', '20:00', 9),
(10, 'AA134', 'Dallas', '2024-11-10', '18:00', 'Miami', '2024-11-10', '22:30', 10);

-- Car_Comp Table
INSERT INTO Car_Comp (Comp_ID, Comp_Name, Pickup_Loc, Dropoff_Loc, Comp_Policy, Comp_Email, Comp_PhoneNum, Comp_Website) VALUES
(1, 'Sixt', 'Cairo Airport', 'Cairo City Center', 'No smoking in car', 'sixt@car.com', '01234567890', 'www.sixt.com'),
(2, 'Avis', 'Alexandria Airport', 'Alexandria City Center', 'No pets allowed', 'avis@car.com', '01234567891', 'www.avis.com'),
(3, 'Hertz', 'Sharm El-Sheikh Airport', 'Sharm El-Sheikh City Center', 'Fuel policy: full to full', 'hertz@car.com', '01234567892', 'www.hertz.com'),
(4, 'Budget', 'Luxor Airport', 'Luxor City Center', 'Insurance included', 'budget@car.com', '01234567893', 'www.budget.com'),
(5, 'Enterprise', 'Cairo Airport', 'Giza', 'Free cancellation within 24 hours', 'enterprise@car.com', '01234567894', 'www.enterprise.com'),
(6, 'Dollar', 'Hurghada Airport', 'Hurghada City Center', 'Late fees apply', 'dollar@car.com', '01234567895', 'www.dollar.com'),
(7, 'Alamo', 'Marsa Alam', 'Marsa Alam City Center', 'No extra charges for additional drivers', 'alamo@car.com', '01234567896', 'www.alamo.com'),
(8, 'National', 'Sharm El-Sheikh Airport', 'Sharm El-Sheikh City Center', 'No delivery service', 'national@car.com', '01234567897', 'www.nationalcar.com'),
(9, 'Europcar', 'Cairo Airport', 'Giza', 'Free GPS', 'europcar@car.com', '01234567898', 'www.europcar.com'),
(10, 'Thrifty', 'Luxor Airport', 'Luxor City Center', 'No smoking in car', 'thrifty@car.com', '01234567899', 'www.thrifty.com');

-- Customer Table
INSERT INTO Customer (Cust_ID, Cust_Name, Cust_PhoneNum, Cust_Email, Cust_Address, Nationality, Bank_Acc, Date_Birth, Credit_Worthiness) VALUES
(1, 'Ahmed Ali', '01001234567', 'ahmed@domain.com', '123 Cairo St.', 'Egyptian', 'EG123456789', '1990-05-01', 'Good'),
(2, 'Sara Mohamed', '01002345678', 'sara@domain.com', '456 Alexandria St.', 'Egyptian', 'EG987654321', '1985-02-10', 'Excellent'),
(3, 'Mona Hassan', '01003456789', 'mona@domain.com', '789 Sharm El-Sheikh St.', 'Egyptian', 'EG234567890', '1993-07-22', 'Fair'),
(4, 'John Doe', '01004567890', 'john.doe@domain.com', '321 New York St.', 'American', 'US123456789', '1980-08-15', 'Excellent'),
(5, 'Emma White', '01005678901', 'emma.white@domain.com', '654 London St.', 'British', 'GB123456789', '1992-03-09', 'Good'),
(6, 'James Smith', '01006789012', 'james.smith@domain.com', '987 Paris St.', 'French', 'FR123456789', '1988-12-04', 'Fair'),
(7, 'Sophia Brown', '01007890123', 'sophia.brown@domain.com', '321 Berlin St.', 'German', 'DE123456789', '1991-06-18', 'Good'),
(8, 'Daniel Taylor', '01008901234', 'daniel.taylor@domain.com', '543 Tokyo St.', 'Japanese', 'JP123456789', '1987-11-25', 'Excellent'),
(9, 'Olivia Williams', '01009123456', 'olivia.williams@domain.com', '876 Rome St.', 'Italian', 'IT123456789', '1995-01-30', 'Fair'),
(10, 'Lucas Johnson', '01010234567', 'lucas.johnson@domain.com', '432 Sydney St.', 'Australian', 'AU123456789', '1986-04-11', 'Good');

-- Orders Table
INSERT INTO Orders (orderID, bookingstatus, products, salesDeptEmpl, Custpref, Ord_Date, Ord_App, Cust_ID) VALUES
(1, 'Confirmed', 'Flight, Hotel, Car Rental', 'Emp01', 'Sea view, Non-smoking', '2024-10-01', '2024-10-02', 1),
(2, 'Pending', 'Flight, Hotel', 'Emp02', 'Near the pool', '2024-10-05', '2024-10-06', 2),
(3, 'Cancelled', 'Flight', 'Emp03', 'Window seat', '2024-10-07', '2024-10-08', 3),
(4, 'Confirmed', 'Hotel, Car Rental', 'Emp04', 'Near city center', '2024-10-09', '2024-10-10', 4),
(5, 'Completed', 'Flight, Hotel', 'Emp05', 'Ocean view', '2024-10-12', '2024-10-13', 5),
(6, 'Confirmed', 'Flight, Hotel, Car Rental', 'Emp06', 'Quiet room', '2024-10-14', '2024-10-15', 6),
(7, 'Pending', 'Flight', 'Emp07', 'Aisle seat', '2024-10-16', '2024-10-17', 7),
(8, 'Confirmed', 'Hotel', 'Emp08', 'Sea view, Non-smoking', '2024-10-18', '2024-10-19', 8),
(9, 'Cancelled', 'Car Rental', 'Emp09', 'GPS required', '2024-10-20', '2024-10-21', 9),
(10, 'Completed', 'Flight, Hotel, Car Rental', 'Emp10', 'Near airport', '2024-10-22', '2024-10-23', 10);

-- Room Table
INSERT INTO Room (H_ID, Room_ID, R_Number, R_Type, R_Price, R_Availability, R_Amenities) VALUES
(1, 101, 'R001', 'Deluxe', 200, 1, 'Free Wi-Fi, Sea view'),
(2, 102, 'R002', 'Standard', 120, 0, 'Free Wi-Fi'),
(3, 103, 'R003', 'Suite', 350, 1, 'Free Wi-Fi, Mini-bar, Balcony'),
(4, 104, 'R004', 'Family', 180, 0, 'Free Wi-Fi, Pool view'),
(5, 105, 'R005', 'Superior', 220, 1, 'Free Wi-Fi, Spa access'),
(6, 106, 'R006', 'Deluxe', 240, 0, 'Free Wi-Fi, Sea view, Non-smoking'),
(7, 107, 'R007', 'Standard', 150, 1, 'Free Wi-Fi, Pool view'),
(8, 108, 'R008', 'Suite', 400, 1, 'Free Wi-Fi, Mini-bar, Balcony'),
(9, 109, 'R009', 'Family', 250, 0, 'Free Wi-Fi, Beachfront view'),
(10, 110, 'R010', 'Superior', 230, 1, 'Free Wi-Fi, Breakfast included');

-- Seat Table
INSERT INTO Seat (F_ID, Seat_ID, S_Number, S_Pref, S_Price, S_Availability) VALUES
(1, 201, 'S001', 'Window', 500, 1),
(2, 202, 'S002', 'Aisle', 450, 0),
(3, 203, 'S003', 'Window', 550, 1),
(4, 204, 'S004', 'Middle', 400, 0),
(5, 205, 'S005', 'Aisle', 470, 1),
(6, 206, 'S006', 'Window', 520, 1),
(7, 207, 'S007', 'Middle', 430, 1),
(8, 208, 'S008', 'Window', 510, 0),
(9, 209, 'S009', 'Aisle', 480, 1),
(10, 210, 'S010', 'Window', 530, 0);

-- Car Table
INSERT INTO Car (Comp_ID, Car_ID, License_Num, Model, Make, C_Type, C_Year, Trans_Type, Num_Seats, Features, Fuel_Type, Rental_Price, Cust_ID) VALUES
(1, 301, 'ABC1234', 'SUV', 'Toyota', '4x4', '2021', 'Automatic', 5, 'GPS, AC', 'Gasoline', 50, 1),
(2, 302, 'XYZ5678', 'Sedan', 'Honda', 'Luxury', '2020', 'Automatic', 4, 'Leather seats, Sunroof', 'Gasoline', 40, 2),
(3, 303, 'LMN7890', 'Hatchback', 'Ford', 'Compact', '2019', 'Manual', 4, 'Bluetooth, AC', 'Diesel', 30, 3),
(4, 304, 'OPQ4321', 'SUV', 'Jeep', '4x4', '2022', 'Automatic', 7, 'GPS, Heated seats', 'Gasoline', 60, 4),
(5, 305, 'RST5432', 'Convertible', 'BMW', 'Luxury', '2021', 'Automatic', 2, 'Leather seats, Sunroof', 'Electric', 70, 5),
(6, 306, 'UVW6543', 'Minivan', 'Kia', 'Family', '2018', 'Manual', 8, 'Bluetooth, AC', 'Diesel', 45, 6),
(7, 307, 'XYZ7654', 'Coupe', 'Audi', 'Luxury', '2020', 'Automatic', 4, 'Sunroof, Leather seats', 'Gasoline', 65, 7),
(8, 308, 'PQR8765', 'SUV', 'Nissan', '4x4', '2022', 'Automatic', 5, 'GPS, Roof rack', 'Gasoline', 55, 8),
(9, 309, 'DEF2345', 'Hatchback', 'Volkswagen', 'Compact', '2021', 'Manual', 4, 'Bluetooth, AC', 'Gasoline', 35, 9),
(10, 310, 'LMN8765', 'Sedan', 'Mazda', 'Luxury', '2020', 'Automatic', 4, 'Sunroof, Heated seats', 'Diesel', 50, 10);

-- Payment Table
INSERT INTO Payment (OrderID, Pay_RefNum, Paid_Amount, payStatus, Discount, Conditions) VALUES
(1, 'P001', 550, 'Completed', 10, 'Full payment received'),
(2, 'P002', 380, 'Pending', 0, 'Awaiting payment confirmation'),
(3, 'P003', 500, 'Completed', 5, 'Discount applied for early booking'),
(4, 'P004', 450, 'Completed', 0, 'Full payment received'),
(5, 'P005', 670, 'Completed', 15, 'Discount applied for package booking'),
(6, 'P006', 400, 'Pending', 0, 'Awaiting payment confirmation'),
(7, 'P007', 460, 'Completed', 10, 'Discount applied for loyalty program'),
(8, 'P008', 520, 'Completed', 0, 'Full payment received'),
(9, 'P009', 480, 'Cancelled', 0, 'Refund processed'),
(10, 'P010', 550, 'Completed', 5, 'Discount applied for group booking');

-- Traveled_with Table
INSERT INTO Traveled_with (Cust_ID, Air_ID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 1),
(6, 2),
(7, 3),
(8, 4),
(9, 1),
(10, 2);

-- Room_booked Table
INSERT INTO Room_booked (Ord_ID, Cust_ID, H_ID, Room_ID) VALUES
(1, 1, 1, 101),
(2, 2, 2, 102),
(3, 3, 3, 103),
(4, 4, 4, 104),
(5, 5, 5, 105),
(6, 6, 6, 106),
(7, 7, 7, 107),
(8, 8, 8, 108),
(9, 9, 9, 109),
(10, 10, 10, 110);

-- Car_rented Table
INSERT INTO Car_rented (Ord_ID, Cust_ID, Comp_ID, Car_ID) VALUES
(1, 1, 1, 301),
(2, 2, 2, 302),
(3, 3, 3, 303),
(4, 4, 4, 304),
(5, 5, 5, 305),
(6, 6, 6, 306),
(7, 7, 7, 307),
(8, 8, 8, 308),
(9, 9, 9, 309),
(10, 10, 10, 310);

-- Seat_reserved Table
INSERT INTO Seat_reserved (F_ID, Seat_ID, Cust_ID, Ord_ID) VALUES
(1, 201, 1, 1),
(2, 202, 2, 2),
(3, 203, 3, 3),
(4, 204, 4, 4),
(5, 205, 5, 5),
(6, 206, 6, 6),
(7, 207, 7, 7),
(8, 208, 8, 8),
(9, 209, 9, 9),
(10, 210, 10, 10);



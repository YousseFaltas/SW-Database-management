-- Hotel Table
INSERT INTO Hotel (H_id, H_name, H_Loc, H_Policy, H_Email, H_phone, H_Website) VALUES
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
INSERT INTO Airline (Air_ID, Air_Name, Air_Policy, Air_Email, Aie_phone, Air_Website) VALUES
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


-- Car_Comp Table
INSERT INTO Car_Comp (Comp_ID, Comp_Name, Pickup_Loc, Dropoff_Loc, Comp_Policy, Comp_Email, Comp_phone, Comp_Website) VALUES
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
INSERT INTO Customer (Cust_ID, Cust_Name, Cust_phone, Cust_Email, Cust_Address, Nationality, Bank_Acc, Date_Birth, Credit_Worthiness) VALUES
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
INSERT INTO Orders (Ord_id, Booking_status, products, SalesDept_empl, Cust_pref, Ord_Date, Ord_App, Cust_ID) VALUES
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
INSERT INTO Room (H_ID, R_id, R_num, R_Type, R_Price, R_available, R_ameneties) VALUES
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


-- Car Table
INSERT INTO Car (Comp_id, C_id, License_Num, Model, Make, C_Type, C_Year, Trans_Type, Num_Seats, Features, Fuel_Type, Rental_Price) VALUES
(1, 301, 'ABC1234', 'SUV', 'Toyota', '4x4', '2021', 'Automatic', 5, 'GPS, AC', 'Gasoline', 50),
(2, 302, 'XYZ5678', 'Sedan', 'Honda', 'Luxury', '2020', 'Automatic', 4, 'Leather seats, Sunroof', 'Gasoline', 40),
(3, 303, 'LMN7890', 'Hatchback', 'Ford', 'Compact', '2019', 'Manual', 4, 'Bluetooth, AC', 'Diesel', 30),
(4, 304, 'OPQ4321', 'SUV', 'Jeep', '4x4', '2022', 'Automatic', 7, 'GPS, Heated seats', 'Gasoline', 60),
(5, 305, 'RST5432', 'Convertible', 'BMW', 'Luxury', '2021', 'Automatic', 2, 'Leather seats, Sunroof', 'Electric', 70),
(6, 306, 'UVW6543', 'Minivan', 'Kia', 'Family', '2018', 'Manual', 8, 'Bluetooth, AC', 'Diesel', 45),
(7, 307, 'XYZ7654', 'Coupe', 'Audi', 'Luxury', '2020', 'Automatic', 4, 'Sunroof, Leather seats', 'Gasoline', 65),
(8, 308, 'PQR8765', 'SUV', 'Nissan', '4x4', '2022', 'Automatic', 5, 'GPS, Roof rack', 'Gasoline', 55),
(9, 309, 'DEF2345', 'Hatchback', 'Volkswagen', 'Compact', '2021', 'Manual', 4, 'Bluetooth, AC', 'Gasoline', 35),
(10, 310, 'LMN8765', 'Sedan', 'Mazda', 'Luxury', '2020', 'Automatic', 4, 'Sunroof, Heated seats', 'Diesel', 50);

-- Payment Table
INSERT INTO Payment (Ord_id, Pay_RefNum, Paid_Amount, Status, Discount, Conditions) VALUES
(1, 001, 550, 'Completed', 10, 'Full payment received'),
(2, 002, 380, 'Pending', 0, 'Awaiting payment confirmation'),
(3, 003, 500, 'Completed', 5, 'Discount applied for early booking'),
(4, 004, 450, 'Completed', 0, 'Full payment received'),
(5, 005, 670, 'Completed', 15, 'Discount applied for package booking'),
(6, 006, 400, 'Pending', 0, 'Awaiting payment confirmation'),
(7, 007, 460, 'Completed', 10, 'Discount applied for loyalty program'),
(8, 008, 520, 'Completed', 0, 'Full payment received'),
(9, 009, 480, 'Cancelled', 0, 'Refund processed'),
(10, 010, 550, 'Completed', 5, 'Discount applied for group booking');



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




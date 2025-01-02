
-- Room_booked Table
INSERT INTO Room_booked(Ord_ID, Cust_ID, H_ID, R_ID) VALUES
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
INSERT INTO ticket (Air_ID, Ticket_ID, flight_num, Seat_Num, dept_Loc, Arr_loc, Ticket_available, Arr_time, dept_time, class, Ticket_Price)
VALUES
(1, 1001, 'FL123', '12A', 'New York', 'London', 'Available', '2024-12-30 10:00:00', '2024-12-30 06:00:00', 'Economy', 500),
(2, 1002, 'FL124', '15B', 'Paris', 'Tokyo', 'Available', '2024-12-31 14:00:00', '2024-12-31 08:00:00', 'Business', 1200),
(3, 1003, 'FL125', '10C', 'Cairo', 'Dubai', 'Booked', '2024-12-30 18:00:00', '2024-12-30 14:00:00', 'First', 800),
(4, 1004, 'FL126', '22D', 'Sydney', 'Auckland', 'Available', '2024-12-30 16:00:00', '2024-12-30 13:00:00', 'Economy', 300),
(5, 1005, 'FL127', '18E', 'Mumbai', 'Singapore', 'Booked', '2024-12-31 09:00:00', '2024-12-31 04:00:00', 'Business', 700),
(6, 1006, 'FL128', '14F', 'Berlin', 'Amsterdam', 'Available', '2024-12-29 11:00:00', '2024-12-29 09:00:00', 'Economy', 200),
(7, 1007, 'FL129', '5A', 'Los Angeles', 'Mexico City', 'Booked', '2024-12-30 20:00:00', '2024-12-30 17:00:00', 'Economy', 450),
(8, 1008, 'FL130', '8B', 'Seoul', 'Bangkok', 'Available', '2024-12-31 22:00:00', '2024-12-31 19:00:00', 'Economy', 350),
(9, 1009, 'FL131', '6C', 'Cape Town', 'Nairobi', 'Booked', '2024-12-29 15:00:00', '2024-12-29 12:00:00', 'Business', 400),
(10, 1010, 'FL132', '1A', 'Madrid', 'Rome', 'Available', '2024-12-28 20:00:00', '2024-12-28 18:00:00', 'First', 600);

INSERT INTO ticket_reserved (Ord_ID, cust_ID, Air_ID, Ticket_ID)VALUES
(1, 1, 3, 1003),
(2, 2, 5, 1005),
(3, 3, 9, 1009),
(4, 4, 7, 1007),
(5, 5, 2, 1002),
(6, 6, 10, 1010),
(7, 7, 9, 1009),
(8, 8, 6, 1006),
(9, 9, 8, 1008),
(10, 10, 4, 1004);

SELECT 
    O.OrderID,
    O.Ord_Date AS OrderDate,
    O.bookingstatus AS BookingStatus,
    O.products AS ProductsBooked,
    C.Cust_Name AS CustomerName,
    C.Cust_Email AS CustomerEmail,
    P.Paid_Amount AS PaymentAmount,
    P.payStatus AS PaymentStatus
FROM 
    Orders O
INNER JOIN 
    Customer C ON O.Cust_ID = C.Cust_ID
LEFT JOIN 
    Payment P ON O.OrderID = P.OrderID
WHERE 
    O.Ord_Date = (SELECT MAX(Ord_Date) FROM Orders)
LIMIT 1;

SELECT 
    Car.Car_ID,
    Car.Model AS CarModel,
    Car.License_Num AS LicenseNumber,
    Car.Rental_Price AS RentalPrice,
    Car.C_Type AS CarType,
    Car.C_Year AS CarYear,
    C.Cust_Name AS CustomerName,
    O.OrderID,
    O.Ord_Date AS OrderDate
FROM 
    Car_rented CR
INNER JOIN 
    Car ON CR.Comp_ID = Car.Comp_ID AND CR.Car_ID = Car.Car_ID
INNER JOIN 
    Orders O ON CR.Ord_ID = O.OrderID
INNER JOIN 
    Customer C ON O.Cust_ID = C.Cust_ID
WHERE 
    O.Ord_Date = (SELECT MAX(Ord_Date) 
                  FROM Orders O2 
                  INNER JOIN Car_rented CR2 ON O2.OrderID = CR2.Ord_ID)
LIMIT 1;

SELECT 
    A.Air_Name,
    SUM(P.Paid_Amount) AS TotalRevenue
FROM 
    Airline A
INNER JOIN 
    Flight F ON A.Air_ID = F.Air_ID
INNER JOIN 
    Seat S ON F.F_ID = S.F_ID
INNER JOIN 
    Seat_reserved SR ON S.F_ID = SR.F_ID AND S.Seat_ID = SR.Seat_ID
INNER JOIN 
    Orders O ON SR.Ord_ID = O.OrderID
INNER JOIN 
    Payment P ON O.OrderID = P.OrderID
GROUP BY 
    A.Air_Name
ORDER BY 
    TotalRevenue DESC;


SELECT 
    H.hotelName,
    AVG(R.R_Price) AS AverageRoomPrice
FROM 
    Hotel H
INNER JOIN 
    Room R ON H.hotelID = R.H_ID
GROUP BY 
    H.hotelName
ORDER BY 
    AverageRoomPrice DESC;


SELECT 
    O.OrderID,
    O.Ord_Date,
    C.Cust_Name,
    H.hotelName AS HotelName,
    R.R_Number AS RoomNumber,
    F.F_Num AS FlightNumber,
    S.S_Number AS SeatNumber,
    Car.Model AS CarModel,
    Car.License_Num AS LicenseNumber
FROM 
    Orders O
LEFT JOIN 
    Room_booked RB ON O.OrderID = RB.Ord_ID
LEFT JOIN 
    Room R ON RB.H_ID = R.H_ID AND RB.Room_ID = R.Room_ID
LEFT JOIN 
    Hotel H ON R.H_ID = H.hotelID
LEFT JOIN 
    Seat_reserved SR ON O.OrderID = SR.Ord_ID
LEFT JOIN 
    Seat S ON SR.F_ID = S.F_ID AND SR.Seat_ID = S.Seat_ID
LEFT JOIN 
    Flight F ON S.F_ID = F.F_ID
LEFT JOIN 
    Car_rented CR ON O.OrderID = CR.Ord_ID
LEFT JOIN 
    Car ON CR.Comp_ID = Car.Comp_ID AND CR.Car_ID = Car.Car_ID
LEFT JOIN 
    Customer C ON O.Cust_ID = C.Cust_ID
ORDER BY 
    O.Ord_Date DESC;


SELECT 
    H.hotelName AS HotelName,
    MAX(R.R_Price) AS MaxRoomPrice
FROM 
    Room R
INNER JOIN 
    Hotel H ON R.H_ID = H.hotelID
GROUP BY 
    H.hotelName
ORDER BY 
    MaxRoomPrice DESC
LIMIT 1;

SELECT 
    H.hotelName AS HotelName,
    MIN(R.R_Price) AS MinRoomPrice
FROM 
    Room R
INNER JOIN 
    Hotel H ON R.H_ID = H.hotelID
GROUP BY 
    H.hotelName
ORDER BY 
    MinRoomPrice ASC
LIMIT 1;

SELECT 
    A.Air_Name AS AirlineName,
    MIN(S.S_Price) AS MinSeatPrice
FROM 
    Seat S
INNER JOIN 
    Flight F ON S.F_ID = F.F_ID
INNER JOIN 
    Airline A ON F.Air_ID = A.Air_ID
GROUP BY 
    A.Air_Name
ORDER BY 
    MinSeatPrice ASC
LIMIT 1;


SELECT 
    A.Air_Name AS AirlineName,
    MAX(S.S_Price) AS MaxSeatPrice
FROM 
    Seat S
INNER JOIN 
    Flight F ON S.F_ID = F.F_ID
INNER JOIN 
    Airline A ON F.Air_ID = A.Air_ID
GROUP BY 
    A.Air_Name
ORDER BY 
    MaxSeatPrice DESC
LIMIT 1;


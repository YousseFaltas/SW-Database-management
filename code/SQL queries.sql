--first query: total revenue from all orders
SELECT SUM(Paid_Amount) AS Total_Revenue
FROM Payment;
--this is an aggregate query

--second query :average room price per hotel
SELECT H_ID, AVG(R_Price) AS Average_Room_Price
FROM Room
GROUP BY H_ID;
--this is an aggregate query

--third query:customers who have booked rooms
SELECT Cust_Name
FROM Customer
WHERE Cust_ID IN (
    SELECT Cust_ID
    FROM Room_booked
);
--this is a query that uses a sub query to get the customers who have booked a room

--fourth query:hotels with no rooms booked
SELECT H_name
FROM Hotel
WHERE H_ID NOT IN (
    SELECT H_ID
    FROM Room_booked
);
--this is a query that uses a sub query to get the hotel whit no rooms booked

--fifth query : track order and payment details
SELECT C.Cust_Name, O.Ord_ID, P.Status
FROM Customer C
JOIN Orders O ON C.Cust_ID = O.Cust_ID
JOIN Payment P ON O.Cust_ID = P.Cust_ID;

--sixth query:used by car rental companies to track customer rentals and preferences
SELECT C.Cust_Name, Car.Model, CC.Comp_name
FROM Customer C
JOIN Car_rented CR ON C.Cust_ID = CR.Cust_ID
JOIN Car ON CR.Car_ID = Car.C_ID
JOIN Car_Comp CC ON CR.Comp_ID = CC.Comp_id;

--seventh query :used for loyalty programs and targeted marketing
SELECT C.Cust_Name, SUM(P.Paid_Amount) AS Total_Spent
FROM Customer C
JOIN Orders O ON C.Cust_ID = O.Cust_ID
JOIN Payment P ON O.Cust_ID = P.Cust_ID
GROUP BY C.Cust_Name
ORDER BY Total_Spent DESC;

--eigth query :used by airline managers to analyze ticket sales performance
SELECT A.Air_name, COUNT(TR.Ticket_ID) AS Tickets_Reserved
FROM Airline A
JOIN Ticket T ON A.Air_ID = T.Air_ID
JOIN Ticket_reserved TR ON T.Ticket_ID = TR.Ticket_ID
GROUP BY A.Air_name
ORDER BY Tickets_Reserved DESC;
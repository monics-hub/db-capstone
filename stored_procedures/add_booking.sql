DELIMITER //

CREATE PROCEDURE AddBooking (
    IN bookingDate VARCHAR(45),
    IN customerId INT,
    IN locationId INT,
    IN tableNumber INT
)
BEGIN
    INSERT INTO Bookings (Date, idCustomers, idLocation, `Table`)
    VALUES (bookingDate, customerId, locationId, tableNumber);
END //

DELIMITER ;

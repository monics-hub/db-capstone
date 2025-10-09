DELIMITER //

CREATE PROCEDURE UpdateBooking (
    IN bookingId INT,
    IN newDate VARCHAR(45),
    IN newCustomerId INT,
    IN newLocationId INT,
    IN newTableNumber INT
)
BEGIN
    UPDATE Bookings
    SET Date = newDate,
        idCustomers = newCustomerId,
        idLocation = newLocationId,
        `Table` = newTableNumber
    WHERE idBookings = bookingId;
END //

DELIMITER ;

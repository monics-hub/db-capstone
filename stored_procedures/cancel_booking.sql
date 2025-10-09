DELIMITER //

CREATE PROCEDURE CancelBooking (
    IN bookingId INT
)
BEGIN
    DELETE FROM Bookings
    WHERE idBookings = bookingId;
END //

DELIMITER ;

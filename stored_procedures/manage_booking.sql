DELIMITER //

CREATE PROCEDURE ManageBooking (
    IN bookingDate VARCHAR(45),
    IN tableNumber INT
)
BEGIN
    DECLARE bookingCount INT;

    SELECT COUNT(*) INTO bookingCount
    FROM Bookings
    WHERE Date = bookingDate
      AND `Table` = tableNumber;

    IF bookingCount > 0 THEN
        SELECT CONCAT('Table number ', tableNumber, ' is already booked') AS BookingStatus;
    ELSE
        SELECT CONCAT('Table number ', tableNumber, ' is NOT booked yet') AS BookingStatus;
    END IF;
END //

DELIMITER ;


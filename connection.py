import mysql.connector as connector

connection = connector.connect(user = "myuser", password = "MyS3cur3P@ssw0rd!", database="LittleLemon_DB")
cursor = connection.cursor()

def GetMaxQuantity():
    cursor.execute("CALL GetMaxQuantity()")
    while True:
        data = cursor.fetchall()
        for value in data:
            print(value)
        if not cursor.nextset():
            break  # No more result sets


def ManageBooking(bookingDate:str, tableNumber:int): #date in format mm/dd/year like 12/29/2022
    cursor.execute(f"CALL ManageBooking({bookingDate}, {tableNumber})")
    while True:
        data = cursor.fetchall()
        for value in data:
            print(value)
        if not cursor.nextset():
            break


# Insert a new row witht the data provided by the user
def AddBooking(bookingDate:str, customerId:str, locationId:int, tableNumber:int): 
    cursor.execute(f"CALL AddBooking({bookingDate}, {customerId}, {locationId}, {tableNumber})")
    while True:
        data = cursor.fetchall()
        for value in data:
            print(value)
        if not cursor.nextset():
            break


# Will change the date or customerId or locationId or tableNumber based on maintaining the same bookingID
def UpdateBooking(bookingId:int, bookingDate:str, customerId:str, locationId:int, tableNumber:int): 
    cursor.execute(f"CALL UpdateBooking({bookingId}, {bookingDate}, {customerId}, {locationId}, {tableNumber})")
    while True:
        data = cursor.fetchall()
        for value in data:
            print(value)
        if not cursor.nextset():
            break


# Remove a register from the booking table given the id
def CancelBooking(bookingId:int): 
    cursor.execute(f"CALL CancelBooking({bookingId})")
    while True:
        data = cursor.fetchall()
        for value in data:
            print(value)
        if not cursor.nextset():
            break


# Remove a register from the booking table given the id
def ShowLastBookings(numberOfSamples:int): 
    cursor.execute(f"SELECT * FROM Bookings ORDER BY idBookings DESC LIMIT {numberOfSamples}")
    while True:
        data = cursor.fetchall()
        for value in data:
            print(value)
        if not cursor.nextset():
            break


if __name__ == "__main__":
    # Here is a demo of how the program works
    # The max quantity in the orders table can be seen using:
    GetMaxQuantity()
    # Next I add a new booking to the Bookings table
    AddBooking("11/1/2025", "90-000-000", 5, 3)
    # I can see that it was correcly added by calling either manage booking or show last bookings
    ManageBooking("11/1/2025", 3)
    ShowLastBookings(1)
    # Next I proceed to update the booking, and we test manage booking to see how it changes.
    UpdateBooking(51, "11/1/2025", "90-000-000", 5, 4)
    ManageBooking("11/1/2025", 3)
    ManageBooking("11/1/2025", 4)
    ShowLastBookings(1)
    # Finally cancel the booking and make use of showlast bookings to see the change
    CancelBooking(51)
    ShowLastBookings(1)
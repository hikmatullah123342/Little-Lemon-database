import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",  # replace with your MySQL username
    password="your_password",  # replace with your MySQL password
    database="little_lemon"
)

cursor = conn.cursor()

# Function to get the max quantity
def get_max_quantity():
    cursor.execute("CALL GetMaxQuantity()")
    result = cursor.fetchone()
    print(f"Max Quantity: {result[0]}")

# Function to add a booking
def add_booking(booking_data):
    cursor.execute("""
        CALL AddBooking(
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """, booking_data)
    conn.commit()
    print("Booking added successfully.")

# Function to cancel a booking
def cancel_booking(booking_reference):
    cursor.execute("CALL CancelBooking(%s)", (booking_reference,))
    conn.commit()
    print(f"Booking with reference {booking_reference} cancelled.")

# Fetch all bookings
def fetch_all_bookings():
    cursor.execute("SELECT * FROM bookings")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Example usage
if __name__ == "__main__":
    # Fetch max quantity
    get_max_quantity()

    # Add a new booking
    booking_data = (
        '2023-12-24', '99-999-9999', 'John Doe', 'New York', 'USA', '555-5555', 'US',
        150.50, 225.75, 2, 20.00, 180.75, 'Caesar Salad', 'Pizza', 'Tiramisu', 'Red Wine', 'Chardonnay', 'Garlic Bread'
    )
    add_booking(booking_data)

    # Cancel a booking
    cancel_booking('99-999-9999')

    # Fetch and display all bookings
    fetch_all_bookings()

# Close the connection
conn.close()

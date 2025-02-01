import mysql.connector
from mysql.connector import Error

def connect_and_query():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',          # e.g., 'localhost' or '127.0.0.1'
            user='root',      # e.g., 'root'
            password='admin123',  # e.g., 'password'
            database='world'   # e.g., 'test_db'
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object
            cursor = connection.cursor()

            # Example query
            query = "SELECT * FROM city LIMIT 100"  # Replace 'your_table' with your table name
            cursor.execute(query)

            # Fetch and print the results
            results = cursor.fetchall()
            for row in results:
                print(row)

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Call the function
connect_and_query()

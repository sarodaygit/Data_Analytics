import pandas as pd
import mysql.connector
from mysql.connector import Error

class DataFrameConverter:
    """
    Converts MySQL query results into Pandas DataFrame.
    """
    @staticmethod
    def to_dataframe(results, columns):
        """
        Converts raw database results into a Pandas DataFrame and resets the index.
        """
        if results:
            df = pd.DataFrame(results, columns=columns)
            df = df.reset_index(drop=True)  # Reset index to start from 0
            
            # Set Pandas options to display all records
            pd.set_option("display.max_rows", None)  # Show all rows
            pd.set_option("display.max_columns", None)  # Show all columns
            pd.set_option("display.width", None)  # Ensure full width is used
            pd.set_option("display.max_colwidth", None)  # Show full column text
            
            return df
        else:
            print("No data found.")
            return pd.DataFrame(columns=columns)

class MySQLDatabase:
    """
    Handles MySQL database operations.
    """
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """
        Establish a connection to the MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("✅ Connected to MySQL database")
        except Error as e:
            print(f"❌ Error: {e}")

    def disconnect(self):
        """
        Close the database connection.
        """
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("✅ MySQL connection closed")

    def create_city(self, name, country_code, district, population):
        """
        Insert a new city record.
        """
        query = "INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s)"
        values = (name, country_code, district, population)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"✅ City '{name}' added successfully.")
        except Error as e:
            print(f"❌ Error inserting city: {e}")

    def read_cities(self, name=None, country_code=None, district=None, population=None):
        """
        Fetch city records. If no parameters are provided, return all records as raw data.
        """
        try:
            if name is None and country_code is None and district is None and population is None:
                query = "SELECT * FROM city ORDER BY ID ASC"
                self.cursor.execute(query)
            else:
                query = "SELECT * FROM city WHERE 1=1"
                values = []

                if name:
                    query += " AND Name = %s"
                    values.append(name)
                if country_code:
                    query += " AND CountryCode = %s"
                    values.append(country_code)
                if district:
                    query += " AND District = %s"
                    values.append(district)
                if population:
                    query += " AND Population = %s"
                    values.append(population)

                self.cursor.execute(query, tuple(values))

            results = self.cursor.fetchall()
            columns = [col[0] for col in self.cursor.description]  # Extract column names

            if not results:
                print("⚠️ No matching records found.")
            
            return results, columns  # Returning raw data and column names
        except Error as e:
            print(f"❌ Error fetching city: {e}")
            return [], []

    def update_city_population(self, name, country_code, district, population, new_population):
        """
        Update the population of a city identified by name, country, district, and old population.
        """
        try:
            query = """
                UPDATE city SET Population = %s 
                WHERE Name = %s AND CountryCode = %s AND District = %s AND Population = %s
            """
            self.cursor.execute(query, (new_population, name, country_code, district, population))
            self.connection.commit()
            if self.cursor.rowcount:
                print(f"✅ City '{name}' updated with new population: {new_population}")
            else:
                print("⚠️ No matching city found to update.")
        except Error as e:
            print(f"❌ Error updating city: {e}")

    def delete_city(self, name, country_code, district, population):
        """
        Delete a city identified by name, country, district, and population.
        """
        try:
            query = """
                DELETE FROM city 
                WHERE Name = %s AND CountryCode = %s AND District = %s AND Population = %s
            """
            self.cursor.execute(query, (name, country_code, district, population))
            self.connection.commit()
            if self.cursor.rowcount:
                print(f"✅ City '{name}' deleted successfully!")
            else:
                print("⚠️ No matching city found to delete.")
        except Error as e:
            print(f"❌ Error deleting city: {e}")

# Example Usage
if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = "admin123"
    database = "world"

    # Database Configuration
    db = MySQLDatabase(host=host, user=user, password=password, database=database)

    city_name = "New City"
    country_code = "USA"
    district = "New District"
    initial_population = 50000
    updated_population = 75000

    # 1. Create a new city
    db.create_city(city_name, country_code, district, initial_population)

    # 2. Read the newly inserted city
    print("\n📌 After Insertion:")
    results, columns = db.read_cities(city_name, country_code, district, initial_population)
    print(results)  # Print raw data

    # 3. Update the population from 50000 to 75000
    db.update_city_population(city_name, country_code, district, initial_population, updated_population)

    # 4. Read again to confirm update
    print("\n📌 After Update:")
    results, columns = db.read_cities(city_name, country_code, district, updated_population)
    print(results)  # Print raw data

    # 5. Delete the city
    db.delete_city(city_name, country_code, district, updated_population)

    # 6. Read again to confirm deletion
    print("\n📌 After Deletion:")
    results, columns = db.read_cities(city_name, country_code, district, updated_population)
    print(results)  # Should return empty

    # Fetch all cities
    results, columns = db.read_cities()

    # Convert to DataFrame using DataFrameConverter
    # df = DataFrameConverter.to_dataframe(results, columns)

    # Print the DataFrame
    # print("\n📌 City DataFrame:")
    # print(df)

    # Disconnect
    db.disconnect()

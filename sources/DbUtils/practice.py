import mysql.connector
from mysql.connector import Error
import pandas as pd

class DataFrameConverter:
    def to_dataframe(results, columns):
        if results:
            df = pd.DataFrame(results, columns=columns)
            df = df.reset_index(drop=True)
            pd.set_option("display.max_rows", None)
            pd.set_option("display.max_columns", None)
            pd.set_option("display.width", None)
            pd.set_option("display.max_colwidth", None)
            return df
        else:
            print("No data found.")
            return pd.DataFrame(columns=columns)    


class MySQLClient:
    def __init__(self, host, port, password, user, database):
        print("MySQLClient.__init__()")
        self.host = host
        self.port = port
        self.password = password
        self.user = user
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()
    
    def connect(self):
        print("MySQLClient.connect()")
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")


    def disconnect(self):
        print("MySQLClient.disconnect()")
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection closed")
    
    # def read_cities(self, name=None, country_code=None, district=None, population=None):
        # print("MySQLClient.read_cities()")
        # query = "SELECT * FROM city WHERE"
        # conditions = []
        # if name:
        #     conditions.append(f"Name = '{name}'")
        # if country_code:
        #     conditions.append(f"CountryCode = '{country_code}'")
        # if district:
        #     conditions.append(f"District = '{district}'")
        # if population:
        #     conditions.append(f"Population = {population}")
        # query += " AND ".join(conditions)
        # print(f"Query: {query}")
        # try:
        #     self.cursor.execute(query)
        #     records = self.cursor.fetchall()
        #     columns = [column[0] for column in self.cursor.description]
        #     if records:
        #         return pd.DataFrame(records, columns=columns)
        #     else:
        #         print("No data found.")
        #         return pd.DataFrame(columns=columns)
        # except Error as e:
        #     print(f"Error reading cities: {e}")
        #     return pd.DataFrame(columns=columns)

    def read_cities_all(self):
        """
        Fetch all city records from the database.
        """
        print("MySQLClient.read_cities()")
        try:
            query = "SELECT * FROM city ORDER BY ID ASC"
            self.cursor.execute(query)

            results = self.cursor.fetchall()
            columns = [col[0] for col in self.cursor.description]  # Extract column names

            if not results:
                print("No records found.")

            return results, columns  # Returning raw data and column names
        except Error as e:
            print(f" Error fetching cities: {e}")
            return [], []
    
    def someothertable(self):
        try:
            print("implement logic for different table")
        except Error as e:
            print("Error occured")
if __name__ == '__main__':
    print("this is mysql client program")
    client = MySQLClient(host="localhost", port=3306, user="root", password="admin123", database="world")
    cities, columns = client.read_cities_all()
    df = DataFrameConverter.to_dataframe(cities, columns)
    # print(df)
    print(df.shape)

    # if cities:
    #     print(columns)
    #     for city in cities:
    #         print(city)
    client.disconnect()

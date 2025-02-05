import pandas as pd
import csv

# -------------------------------------------------------------------
# Example 1: Reading CSV manually using built-in file I/O methods
# -------------------------------------------------------------------
# This block (commented out) demonstrates how to open and read a CSV file
# using Python's built-in functions. It reads the entire file into a list of lines,
# strips whitespace, splits each line by commas, and then prints the city name, country,
# and population from each row.
# with open('sample-pandas.csv', 'r') as file:
#     reader = file.readlines()  # Read all lines from the file
#     # Optionally, you can print each raw row:
#     # for row in reader:
#     #     print(row)
#     # Split each line by commas and remove any extra whitespace
#     rows = [row.strip().split(',') for row in reader]
#     # Loop through the rows and print formatted output for each
#     for row in rows:
#         print(f'city name = {row[0]}, country = {row[1]} population = {row[2]}')

# -------------------------------------------------------------------
# Example 2: Reading CSV using the csv module
# -------------------------------------------------------------------
# This block (commented out) uses the csv module, which handles CSV parsing robustly.
# It reads each row into a list, then extracts and converts the population values (skipping the header)
# before printing them.
# with open('sample-pandas.csv', 'r') as file:
#     reader = csv.reader(file)  # Create a CSV reader object
#     rows = [row for row in reader]  # Convert the reader to a list of rows
#     # Loop through rows to print each city's details (if needed)
#     # for row in rows:
#     #     print(f'city name = {row[0]}, country = {row[1]} population = {row[2]}')  
#     # Extract population values (skipping header row) and convert to integers
#     population = [int(row[2]) for row in rows[1:]]
#     print(f'population = {population}')

# -------------------------------------------------------------------
# Set display options for pandas DataFrames
# -------------------------------------------------------------------
# This ensures that all rows are displayed (no truncation) and that floats are shown
# using their string representation instead of scientific notation.
pd.set_option('display.max.rows', None)
pd.set_option('display.float_format', str)

# -------------------------------------------------------------------
# Read CSV into a pandas DataFrame
# -------------------------------------------------------------------
# The CSV file is read into a DataFrame called 'data'. This allows for easy data manipulation.
data = pd.read_csv('sample-pandas.csv')
# The following print statements (commented out) can be used to inspect the DataFrame:
# print(data)                         # Display the entire DataFrame.
# print(data['population'])           # Display just the 'population' column.
# print(data['population'].to_list()) # Convert the 'population' column to a list and print it.
# print(data.shape)                   # Print the dimensions (rows, columns) of the DataFrame.
# print(data.info())                  # Print a concise summary of the DataFrame.
# print(data.describe())              # Print summary statistics for numeric columns.
# print(data.describe(include='all')) # Print summary statistics for all columns.

# -------------------------------------------------------------------
# Example: Creating and using pandas Series
# -------------------------------------------------------------------
# Create a Series with custom index labels.
# seriessample = pd.Series([1000, 2000, 3000, 4000, 5000], index=['a', 'b', 'c', 'd', 'e'])
# print(seriessample[0])  # Access and print the first element of the Series.

# Create a Series with colors and a custom numeric index.
# colors = pd.Series(['red', 'green', 'blue', 'yellow', 'black'], index=[1,2,3,4,5])
# Demonstrate different methods of accessing elements:
# print(colors[1])         # Access by key (numeric index).
# print(colors.loc[4])     # Access using label-based indexing.
# print(colors.iloc[4])    # Access using integer-location based indexing.
# print(colors.loc[0:3])   # Access a range of labels (inclusive of both endpoints).
# print(colors.iloc[0:3])  # Access a slice using integer-location based indexing.
# print(colors.iloc[-1])   # Access the last element.

# -------------------------------------------------------------------
# Creating a DataFrame from Series
# -------------------------------------------------------------------
# Create a Series for population data with city names as indices.
population = pd.Series([1000, 2000, 3000, 4000, 5000],
                       index=['London', 'Berlin', 'Tokyo', 'Rome', 'Paris'])
# Create a Series for office location data (note: fewer entries than the population Series).
offic_location = pd.Series([10, 20, 30],
                           index=['London', 'Berlin', 'Tokyo'])
# Combine the two Series into a single DataFrame.
city_data = pd.DataFrame({'population': population, 'office_location': offic_location})
# Uncomment the following lines to inspect various parts of the DataFrame:
# print(f'city data {city_data}')                      # Print the entire DataFrame.
# print(f'population data \n {city_data["population"]}')  # Print just the 'population' column.
# print(f'population london data {city_data["population"]["London"]}')  # Print London's population.
# print(f'london data in city data {city_data.loc["London"]}')            # Print all data for London.
# print(city_data.keys())                              # Print the column names.
# print(city_data.index)                               # Print the row indices.
# print(city_data.iloc[0])                             # Print the first row using integer-location indexing.
# print(city_data.iloc[0].index)                       # Print the index labels of the first row.

# -------------------------------------------------------------------
# DataFrame filtering examples (commented out)
# -------------------------------------------------------------------
# The following examples show how to filter the main DataFrame 'data' using boolean indexing:
# print(data.iloc[-20:])                             # Display the last 20 rows.
# new_data = data[data.population > 1000000]          # Filter rows with population greater than 1,000,000.
# new_data = data[data.country]                       # Incorrect usage: tries to use the 'country' column as a boolean mask.
# new_data = data[data.country == 'Russia']           # Correct filtering: select rows where country is 'Russia'.

# Additional examples for working with the 'country' column:
# print(data.country)                                 # Print the entire 'country' column.
# print(data['country'].unique())                     # Print unique country names.
# no_null_new_data = data[data.population.notnull()]  # Filter out rows where population is null.
# print(no_null_new_data)

# Filtering the city_data DataFrame to show only rows with non-null 'office_location':
# print(city_data[city_data.office_location.notnull()])

# -------------------------------------------------------------------
# String filtering on the 'name' column in the DataFrame (if such a column exists)
# -------------------------------------------------------------------
# Filter rows where the city name contains the letter 'a' (case-insensitive):
# citieswithA = data[data.name.str.contains('a', case=False)]
# print(citieswithA)
#
# Filter rows where the city name starts with 'A' or 'Al':
# citiesstartswithA = data[data.name.str.startswith('A')]
# citiesstartswithA = data[data.name.str.startswith('Al')]
# print(citiesstartswithA)
#
# Filter rows where the city name ends with 'e', or ends with 'e' and the country is 'Germany':
# citiesendswithA = data[data.name.str.endswith('e')]
# citiesendswithA = data[(data.name.str.endswith('e')) & (data.country == 'Germany')]
# print(citiesendswithA)
#
# Filter rows for cities in Spain with a population over 500,000:
# citiesofspanish = data[(data.country == 'Spain') & (data.population > 500000)]
# print(citiesofspanish)

# -------------------------------------------------------------------
# Calculating and filtering by summary statistics
# -------------------------------------------------------------------
# Calculate the average population of all cities and print it.
# average_population = int(data['population'].mean())
# print(f'average population = {average_population}')
#
# Filter cities in France with a population greater than the average population:
# citisoffrance = data[(data.population > average_population) & (data.country == 'France')]
# print(citisoffrance)
#
# Print the mean population and the sum of populations grouped by country:
# print(data.population.mean())
# print(data.groupby('country', sort=False).population.sum())

# -------------------------------------------------------------------
# Grouping data and exporting results
# -------------------------------------------------------------------
# Group the DataFrame by the 'country' column and count the number of cities (assuming the 'name' column holds city names).
# citycount = data.groupby('country', sort=False).name.count()
# print(citycount)  # Display the count of cities per country

# Export the grouped city count data to a CSV file named 'citycount.csv'.
# citycount.to_csv('citycount.csv', header=True)

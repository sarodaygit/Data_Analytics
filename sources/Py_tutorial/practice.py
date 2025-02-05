import pandas as pd
import csv

# data = pd.read_csv('sample-pandas.csv')
# data = pd.read_csv('C:\\Users\\ashwini\\OneDrive\\Docum
# print(pd.__version__)
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', str)
data = pd.read_csv("sample-pandas.csv")
# print(data)
# print(data.country.unique())
# citiesA = data[data.name.str.startswith('A', na=False)]
citiesA = data[data.name.str.contains('a', case=False)]
citiesA = data[data.name.str.]
print(citiesA)
# print(data.shape)
# print(data.info())
# print(data.describe(include='all'))
# # print(data['population'])
















# colors = pd.Series(['red', 'green', 'blue', 'yellow', 'black'], index=[1, 2, 3, 4, 5])
# print(colors)
# print(colors[1])
# print(colors.loc[1])
# print(colors.iloc[0])

# population = pd.Series([1000, 2000, 3000, 4000, 5000], index=['London', 'Berlin','Tokyo', 'Rome', 'Paris'])
# office_location = pd.Series([10,20,30], index=['London', 'Berlin', 'Tokyo'])
# city_data = pd.DataFrame({'population': population, 'office_location': office_location})
# print(city_data)
# # print(city_data['population'])
# # print(city_data['population']['London'])    
# # print(city_data.loc['London'])
# print(city_data.iloc[0])
import pandas as pd
import csv

# with open('sample-pandas.csv', 'r') as file:
#     reader = file.readlines()
#     # for row in reader:
#     #     print(row)
#     rows = [row.strip().split(',') for row in reader]
#     for row in rows:
#         print(f'city name = {row[0]}, country = {row[1]} population = {row[2]}')

# with open('sample-pandas.csv', 'r') as file:
#     reader = csv.reader(file)
#     rows = [row for row in reader]
#     # for row in rows:
#     #     print(f'city name = {row[0]}, country = {row[1]} population = {row[2]}')  
#     population = [int(row[2]) for row in rows[1:]]
#     print(f'population = {population}')

# pd.set_option('display.max.rows', None)
# pd.set_option('display.float_format', str)
# data = pd.read_csv('sample-pandas.csv')
# print(data)
# print(data['population'])
# print(data['population'].to_list())
# print(data.shape)
# print(data.info())
# print(data.describe())
# print(data.describe(include='all'))


colors = pd.Series(['red', 'green', 'blue', 'yellow', 'black'], index=[1,2,3,4,5])

# print(colors[1])
# print(colors.loc[4])
# print(colors.iloc[4])
print(colors.loc[0:3])
print(colors.iloc[0:3])
print(colors.iloc[-1])

# population = pd.Series([1000, 2000, 3000, 4000, 5000], index=['London', 'Berlin', 'Tokyo', 'Rome', 'Paris'])
# offic_location = pd.Series([10,20,30], index=['London', 'Berlin', 'Tokyo' ])
# city_data = pd.DataFrame({'population': population, 'office_location': offic_location})
# print(f'city data {city_data}') 
# print(f'population data \n {city_data['population']}')
# print(f'population london data {city_data['population']['London']}')
# print(f'london data in city data {city_data.loc['London']}')
# print(city_data.keys())
# print(city_data.index) 
# print(city_data.iloc[0])
# print(city_data.iloc[0].index)

# print(data.iloc[-20:])
# new_data = data[data.population > 1000000]
# new_data = data[data.country]
# new_data = data[data.country == 'Russia']
# print(data.country)
# print(data['country'].unique())
# no_null_new_data = data[data.population.notnull()]
# print(no_null_new_data)

# print(city_data[city_data.office_location.notnull()])

# citieswithA = data[data.name.str.contains('a', case=False)]
# print(citieswithA)

# citiesstartswithA = data[data.name.str.startswith('A')]
# citiesstartswithA = data[data.name.str.startswith('Al')]
# print(citiesstartswithA)
# citiesendswithA = data[data.name.str.endswith('e')]
# citiesendswithA = data[(data.name.str.endswith('e')) & (data.country == 'Germany')]
# print(citiesendswithA)

# citiesofspanish = data[(data.country == 'Spain') & (data.population > 500000)]
# print(citiesofspanish)

# average_population = int(data['population'].mean())
# print(f'average population = {average_population}')

# citisoffrance = data[(data.population >  average_population) & (data.country == 'France')]
# print(citisoffrance)

# print(data.population.mean())
# print(data.groupby('country', sort=False).population.sum())
# citycount = data.groupby('country', sort=False).name.count()
# print(citycount)
# citycount.to_csv('citycount.csv', header=True)
# with open('weather_data.csv') as data:
#     weather_data = data.readlines()
#     print(weather_data)

# import csv
#
# with open('weather_data.csv') as data:
#     weather_data = csv.reader(data)
#     # print(weather_data)  # csv reader object
#     temperatures = []
#     for row in weather_data:
#         if row[1] != 'temp':  # temp(name of the column) is also there
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(data)
# print(type(data))   #  ->  dataframe
# # prints columns
# print(data['temp'])    #  ->  series

# print(data.to_json())
# print(data.to_dict())
# temperatures = data['temp'].to_list()

# print(sum(temperatures)/len(temperatures))
# print(data['temp'].max())

# # prints rows
# print(data[data.day == 'Monday'])
# print(data[data.day == 'Monday'].temp)

# print(data[data.temp == data.temp.max()])

# t = data[data.day == 'Monday'].temp
# t = 9 / 5 * t + 32
# print(t)

# # create csv from data
# data_dict = {
#     'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#     'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#     'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
# print(data)

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240526.csv')
# print(data['Primary Fur Color'].unique())
count_data = data.groupby('Primary Fur Color')['Unique Squirrel ID'].count().reset_index()
count_data.rename(columns={'Unique Squirrel ID': 'Count'}, inplace=True)
print(count_data)
count_data.to_csv('squirrel_count.csv')

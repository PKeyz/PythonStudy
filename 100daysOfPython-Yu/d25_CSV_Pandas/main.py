

"""data = []
with open('./weather_data.csv') as weather_data:
    data = weather_data.readlines()

print(data)

import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))


print(temperatures)


data = pandas.read_csv('./weather_data.csv')

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

#print('average Temperature: ' + str(round(sum(temp_list)/len(temp_list),2)) )

average_temp = data['temp'].mean()

max_temp = data['temp'].max()
print(max_temp)

print(data.condition)
equal to data['condition']

get data from data frame rows
print(data[data.temp == max_temp])

monday = data[data.day == 'Monday']

print((float(monday.temp[0])) * (9/5) + 32)
"""

import pandas as pd

data_squirrel = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#whole cvs file as data frame
#print(data_squirrel)

primary_fur = data_squirrel['Primary Fur Color']

count_gray = primary_fur.value_counts()['Gray']
count_cinnamon = primary_fur.value_counts()['Cinnamon']
count_black = primary_fur.value_counts()['Black']

# print(count_black)
# print(count_cinnamon)
# print(count_gray)

df = pd.DataFrame({'Fur Color': ['gray', 'black', 'cinnamon'], 'Count': [count_gray, count_cinnamon, count_black]})

df.to_csv("squirrel_count.csv")
print(df)

#absofuckinglutely NOT satisfactory! I am dissapointed and my day is ruined
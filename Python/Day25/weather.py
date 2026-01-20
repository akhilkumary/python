# with open('weather_data.csv', mode='r') as f:
#     lines = f.readlines()

# print(lines)

import csv

temperatures = []
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)

    for row in data:
        print(row)
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(f'{temperatures}')

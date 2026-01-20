import pandas as pd

data = pd.read_csv('weather_data.csv')

print(data)
print(data['temp'])

# Dataframe
print(type(data))

# Series
print(type(data['temp']))

temp_list = data['temp'].to_list()
print(len(temp_list))

print(f'Average Temp: {round(sum(temp_list) / len(temp_list), 2)}')

print(f"Max Temp: {data['temp'].max()}")

# Columns
print(data.condition)
print(data["condition"])

# Rows
print(data[data.day == 'Monday'])

# Row with max temperature
print(f"Row with Max temperature:\n {data[data.temp == data['temp'].max()]}")

# convert celsius to fahrenheit
temp_in_f = []
for i in range(0, len(data.temp)):
    temp_in_f.append(int(data.temp[i]) * 1.8 + 32)
    # f = c * 1.8 + 32

data.insert(2, "temp_in_f", temp_in_f, True)
print(f"{data}")

# Creating dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [30, 45, 60]
}
df = pd.DataFrame(data_dict)

print(df)
df.to_csv('new_data.csv')
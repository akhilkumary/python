import pandas as pd

squirrel = pd.read_csv('squirrel_data.csv')

# print(squirrel['Primary Fur Color'])

# print(squirrel['Primary Fur Color'].count())
# print(type(squirrel['Primary Fur Color'].value_counts()))
# print(squirrel['Primary Fur Color'].value_counts())

data_dict = {
    "Fur Color" : [],
    "Count": []
}

for key, count in squirrel['Primary Fur Color'].value_counts().items():
    data_dict["Fur Color"].append(key)
    data_dict["Count"].append(count)

df = pd.DataFrame(data_dict)

print(df)

df.to_csv('squirrel_count.csv')

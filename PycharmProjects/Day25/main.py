import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

value = max(temp_list)
print(value)

print(data["temp"].mean())

# get the data in column
print(data["condition"])

# get Data in Row
print(data[data.day == "monday"])
print(data[data.temp == data.temp.max()])

# create a dataframe from scratch
data_dict = {
    "students": ["saurabh", "shubham", "shivam"],
    "scores": [76, 56, 84]
}
data = pandas.DataFrame(data_dict)

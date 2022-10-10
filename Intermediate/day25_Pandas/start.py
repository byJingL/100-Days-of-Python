# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as weather:
#     weather_data = csv.reader(weather)
#     # object
#     print(weather_data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
import pandas

# Dataframe
data = pandas.read_csv("weather_data.csv")
# Series
temp = data["temp"]

data_dict = data.to_dict()
temp_list = temp.to_list()

# remember sun() function
aver_temp = sum(temp_list) / len(temp_list)
print(aver_temp)
# pandas method
print(temp.mean())
max_temp = temp.max()
print(max_temp)

# 2 Ways Get Data in Columns
print(data["condition"])  # like dictionary
print(data.condition)  # like object

# Get Data in Row
# condition in ()
print(data[data.temp == data.temp.max()])
Monday = data[data.day == "Monday"]
temp_f = Monday.temp * 9/5 + 32
print(temp_f)

# Create a  DataFrame from scratch
data_dic = {
    "students": ["Amy", "James", "Emma"],
    "scores": [76, 65, 87],
}
new = pandas.DataFrame(data_dic)
print(new)
new.to_csv("new.csv")

# squirrels data analyzing
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.iloc[0])
# Just use Pandas
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

fur_color_list = data["Primary Fur Color"].to_list()
# print(fur_color_list)
num_black = 0
num_gray = 0
num_cinnamon = 0
for color in fur_color_list:
    if color == "Black":
        num_black += 1
    elif color == "Gray":
        num_gray += 1
    elif color == "Cinnamon":
        num_cinnamon += 1

fur_color_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [num_gray, num_cinnamon, num_black],
}
df = pandas.DataFrame(fur_color_data)
print(df)
df.to_csv("Squirrel_Count.csv")




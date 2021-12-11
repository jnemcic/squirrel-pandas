import pandas

data = pandas.read_csv("Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Number of instances": [grey_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrels_Data_Fur_Color")

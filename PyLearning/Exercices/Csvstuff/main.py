import pandas
# import matplotlib.pyplot as plt
# from prettytable import PrettyTable

#data = pandas.read_csv("Exercices/Csvstuff/weather_data.csv")

# table = PrettyTable()
# table.field_names = data.columns.tolist()
# for index, row in data.iterrows():
#     table.add_row(row.values)
# print(table)


# to_dict = data.to_dict()
# # print(to_dict)

# to_aList = data["temp"].to_list()

# #without pandas
# average = sum(to_aList) / len(to_aList)

# #with pandas
# avr = data["temp"].mean()

# maximum = data["temp"].max()
# print(f"Temperature average : {round(average,1)}")
# print(f"Temperature average : {round(avr,1)}")
# print(f"Temperature max : {maximum}")

# monday = data[data.day == "Monday"]

# tmp = monday["temp"]
# print(f"Temp celsius : {tmp}\nTemp Fahr : {(tmp * 1.8) + 32}")


# Openeing a CSV file which contains some datas about squirrels in Central Park
# Findind how much squirrels are grey, red and black
# Finally creating new csv file with these datas 

# squirrels = pandas.read_csv("Exercices/Csvstuff/centralPark.csv")

# gray = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
# red = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
# black = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

# new_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count" :[gray,red,black]
# }

# data = pandas.DataFrame(new_dict)
# data.to_csv("Exercices/Csvstuff/final.csv")
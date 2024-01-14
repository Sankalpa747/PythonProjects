
# Older way and very difficulty manipulate the data
# # Open the weather data file in read mode
# with open(file="./weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)

# Better than before but still lots of work
# # Better way to use csv library
# import csv
#
# with open(file="./weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#
#     temperatures = []
#
#     for row in data:
#         value = row[1]
#         if not value.isalpha():
#             temperatures.append(int(value))
#
#     print(temperatures)

# # Imports
# import pandas
#
# # Read the CSV (Comma Separated Value) file
# data = pandas.read_csv(filepath_or_buffer="./weather_data.csv")
#
# # Pandas data frame (Table)
# print(f"The type of the panda object: {type(data)}\n")
# print("Print the pandas data frame:")
# print(data)
# print("\n")
#
# # Convert data frame into a dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # Panda data frame has all columns as its attributes
# print(f"Day: {data.day}")
#
# # Get data as rows where the day is Monday
# print(data[data["day"] == "Monday"])
#
# # Get data as a rows where the temp is at max
# print(data[data["temp"] == data["temp"].max()])
#
# # Access data in rows
# monday = data[data["day"] == "Monday"]
# print(f"\nType of the row: {type(monday)}")
# print(monday["temp"])
# print(monday.temp)
#
# # Create a pandas data frame
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# new_df = pandas.DataFrame(data_dict)
# print(f"\n{new_df}\n")
#
# # Create a CSV file from the pandas data frame
# new_df.to_csv("./new_weather_data.csv")
#
# # ---------------------------------------------------------------------------------------------------------------------
#
# # Convert Monday's temperature from celsius into fahrenheit
# # °F = (9/5 × °C) + 32
# monday = data[data.day == 'Monday']
# monday_temp = monday['temp'][0]
# monday_f_temp = (9 / 5 * monday_temp) + 32
# print(f"\nTemp in fahrenheit: {monday_f_temp}")
#
# # Pandas data series (Column)
# temp_data = data["temp"]
# print(f"\nThe type of the temp data: {type(temp_data)}\n")
# print(data["temp"])
#
# # Convert data series into a list
# temp_data_list = temp_data.to_list()
# print(temp_data_list)
#
# # Calculate the average of the temp
# print(f"\nAverage: {temp_data.mean()}")
#
# # Calculate the max of the temp
# print(f"\nMax: {temp_data.max()}")

# ---------------------------------------------------------------------------------------------------------------------

# Squirrel Challenge

# Import pandas
import pandas

# Create the data frame
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240113.csv")
# Print the columns
print(f"Columns: {data.columns}")

# Extract different squirrel color data
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

# Obtain the count of the squirrels
gray_count = gray_squirrels["Primary Fur Color"].count()
red_count = red_squirrels["Primary Fur Color"].count()
black_count = black_squirrels["Primary Fur Color"].count()

# Create squirrel dictionary
squirrel_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}

# Create a new panda data frame from the squirrel dictionary
new_df = pandas.DataFrame(squirrel_dict)

# Export the new data frame into csv file
new_df.to_csv("./squirrel_data.csv")

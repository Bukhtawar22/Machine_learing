import pandas as pd 

# Load dataset
data = pd.read_csv("cars2.csv")

# User input (car ka naam)
user_car = input("Enter car name: ")
# user_year = input("Enter car year: ")

# Check if car exists
if user_car in data['Make'].values:
    price = data.loc[data['Make'] == user_car, 'Max Price'].values
    # make = data.loc[data['Year'] == user_year, 'Make'].values
    print(f"The price of {user_car} and is {price}")
else:
    print("Car not found in dataset.")

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)


# Series
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])

# Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)



# DataFrame
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day2"])
print(df)

# CSV files
csv_path = 'xyz.csv'
df.to_csv(csv_path)
df = pd.read_csv(csv_path)
print(f"CSV file saved to {csv_path}")
print(df.to_string())


print(pd.options.display.max_rows) 


# JSON file
json_path = '/Users/sanghvi/Documents/Coding/Python/Pandas/data.json'
df = pd.read_json(json_path)
# print(df.to_string()) 
print(df.head())
print(df.tail(10))
print(df.info()) 
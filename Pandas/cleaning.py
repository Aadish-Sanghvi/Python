import pandas as pd

csv_path = 'xyz.csv'
df = pd.read_csv(csv_path)
# df.dropna(inplace = True)  # the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
df.fillna(130, inplace = True)

print(df.to_string()) 

x = df["Calories"].mean()
print(x) # we can replace mean, median, mode in table

# Replace NULL values in the "Calories" columns with the number 130:
df["Calories"].fillna(150, inplace = True)

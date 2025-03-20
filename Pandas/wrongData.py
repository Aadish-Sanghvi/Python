import pandas as pd

csv_path = 'xyz.csv'
df = pd.read_csv(csv_path)

#  to convert all cells in the 'Date' column into dates.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace = True)

df.loc[7, 'Duration'] = 45 # Replacing Values

# Replacing values
for x in df.index:
  if df.loc[x, "Calories"] > 400:
    df.loc[x, "Calories"] = 400

# Removing rows
for x in df.index:
  if df.loc[x, "Maxpulse"] > 150:
    df.drop(x, inplace = True)

print(df.head(10))

# Removing duplicates
df.drop_duplicates(inplace = True)
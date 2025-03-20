import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('data.json')
df.plot()
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# df.plot(kind = 'hist', x = 'Duration', y = 'Calories')
plt.show()
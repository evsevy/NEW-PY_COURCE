import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data

start = '2022.03.02'
end = '2023.03.29'

df = data.DataReader('AAPL','yahoo', start, end)
df.head()
plt.plot(df)

ma100 = df.Close.rolling(100).mean()
print(ma100)
plt.plot(ma100, 'r')

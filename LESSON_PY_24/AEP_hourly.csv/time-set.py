#https://www.kaggle.com/robikscube/hourly-energy-consumption#AEP hourly.csv
#https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption?resource=download

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from pylab import rcParams
from pandas.core.nanops import nanmean as pd_nanmean
from sklearn.metrics import mean_squared_error, mean_absolute_error

energy_consumption = pd.read_csv('AEP_hourly.csv', sep=',')
print(energy_consumption.head(2))

print(energy_consumption.AEP_MW.plot(figsize=(15,6),title='consumption', fontsize=14))
plt.show()

plt.figure(figsize=(16,2))
MA = energy_consumption.AEP_MW.rolling(window=24*30*6).mean()
plt.plot(MA)
plt.show()

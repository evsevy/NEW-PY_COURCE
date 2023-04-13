import numpy as np

#create dataset with 100 values that follow a normal distribution
np.random.seed(0)
data = np.random.normal(0,1, 1000)

#view first 10 values
print(data[:10])
import statsmodels.api as sm
import matplotlib.pyplot as plt

#create Q-Q plot with 45-degree line added to plot
fig = sm.qqplot(data, line='45')
plt.show()

#create dataset of 100 uniformally distributed values
data = np.random.uniform(0,1, 1000)

#generate Q-Q plot for the dataset
fig = sm.qqplot(data, line='45')
plt.show()

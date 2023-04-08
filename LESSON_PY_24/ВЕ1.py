from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import learning_curve 
from sklearn.metrics import make_scorer 


np.random.seed(42)

boston_data = load_boston() 
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names) 
target = boston_data.target

mses = []
lstat_coef = range(-20, 23)

for coef in lstat_coef:
    pred_values = np.array([coef * lstat for lstat in boston_df.LSTAT.values])
    mses.append(np.sum((target - pred_values)**2))
    
plt.plot(lstat_coef, mses)

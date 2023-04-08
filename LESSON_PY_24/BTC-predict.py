#https://uproger.com/prognozirovanie-vremennyh-ryadov-kriptovalyut-dlya-chajnikov/

#https://coincodex.com/crypto/bitcoin/historical-data/

#https://github.com/jiwidi/time-series-forecasting-with-python/blob/master/02-Forecasting_models.ipynb


import pandas as pd

coins = pd.read_csv("btc.csv", sep=",", header=0)
coins.set_index("Date", inplace=True)  # make the date become the index
coins = coins.sort_index()

print(coins)

"""
Мы хотим спрогнозировать индекс в этом проекте,
и в какой-то момент времени t мы будем использовать простой метод индексации,
называемый “Равновзвешенный индекс”. Это среднее значение по криптовалюте.
Равный вес – это тип пропорционального метода измерения,
который придаёт одинаковую важность каждой криптовалюте в портфеле,
индексе или индексном фонде. Таким образом,
акции самой маленькой криптовалюты имеют одинаковую
статистическую значимость или вес по сравнению с крупнейшими компаниями,
когда дело доходит до оценки общей эффективности группы.
Следующее уравнение может помочь нам достичь этой цели.
V=(P1W1)+(P2W2)+...+(PnWn)
Значение индекса (V): относится к равновзвешенному индексу.
Цена(P): относится к цене криптовалюты.
Вес (W): относится к присвоенному весу,
но в равновзвешенном индексе каждый вес
равен 1 / N, где N – количество крипты в индексе
"""
result = []

# calculate the index value
for i in range(len(coins.columns)):
    coin = coins[coins.columns[i]] / len(coins.columns)
    result.append(coin)
# assign index value with date
ew_index = pd.DataFrame(1 + pd.DataFrame(pd.concat(result, axis=1)).sum(axis=1))
ew_index.set_axis([*ew_index.columns[:-1], "Index"], axis=1, inplace=True)

print(ew_index.tail(5))



import seaborn as sns
import matplotlib.pyplot as plt

ts_fig, ts_ax = plt.subplots(figsize=(36, 9))
#sns.boxplot(x=ew_index.index.strftime("%Y-%b"), y=ew_index.Index, ax=ts_ax)
ts_ax.set_xlabel("Month", labelpad=9, fontsize=15)
ts_ax.set_ylabel("Total Rides", labelpad=9, fontsize=15)
ts_ax.set_xticklabels(ts_ax.get_xticklabels(), rotation=90)
ts_ax.set_title("Monthly Index", fontsize=21)
plt.show()

from sklearn.preprocessing import MinMaxScaler
data = factors.merge(ew_index, how="left", left_on="Date", right_on="Date")

data_nor = pd.DataFrame(MinMaxScaler().fit_transform(data)).assign(label=data.index) # normalized the data with min-max scaling
data_nor.columns = data.columns.to_list() + ["Date"]
data_nor.set_index("Date", inplace=True)

print(data_nor.tail(5))

data_nor.corr(method="pearson").style.background_gradient(cmap="coolwarm", axis=None).set_precision(2)

cor = data_nor.corr(method="pearson")
data_nor.drop(data_nor.columns[(cor.Index >= -0.2) & (cor.Index <= 0.2)], axis=1, inplace=True) # remove the weak corellation (% between -0.2 to 0.2)

print(data_nor.tail(5))

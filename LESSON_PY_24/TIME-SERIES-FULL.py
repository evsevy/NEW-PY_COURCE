#источник: https://colab.research.google.com/drive/1ldk-Edy1UDv3-SZAr42rRzK6bQ6aLnGJ?usp=sharing#scrollTo=Xr4rkezBtBxI
# импортируем необходимые библиотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from mpl_finance import candlestick_ohlc
import datetime
import matplotlib.dates as mpl_dates
#import mplfinance as mpl

# импортируем файл с данными btc
btc = pd.read_csv("btc2.csv")
print(btc.head())
#btc.plot()
# дату за индекс: все это можно сделать в одну строчку с помощью parse_dates = True
btc = pd.read_csv("btc2.csv", index_col = 'Date', parse_dates = True)
print(btc.head())

# произведем сдвиг на два периода (в данном случае месяца) вперед
btc.shift(2, axis = 0)
print(btc.head())
# рассчитаем скользящее среднее для трех предыдущих месяцев
btc.rolling(window = 3).mean()
print(btc.head())
# построим простой график изменения данных во времени прямо в библиотеке Pandas
btc.plot()
plt.show()
############################################################################
# теперь воспользуемся библиотекой matplotlib для построения сразу двух графиков
#candles:pip install --upgrade mplfinance
#import mplfinance as mpl 
#mpl.plot

# зададим размер графика
plt.figure(figsize = (15,8))

# поочередно зададим кривые (перевозки и скользящее среднее) с подписями и цветом
plt.plot(btc, label = '#BTC', color = 'steelblue')
plt.plot(btc.rolling(window = 6).mean(), label = 'Скользящее среднее за 6 месяцев', color = 'orange')

# добавим легенду, ее положение на графике и размер шрифта
plt.legend(title = '', loc = 'upper left', fontsize = 14)

# добавим подписи к осям и заголовки
plt.xlabel('Месяцы', fontsize = 14)
plt.ylabel('#BTC', fontsize = 14)
plt.title('BTC VOLUMS', fontsize = 16)

# выведем обе кривые на одном графике
plt.show()
#####################################ТРЕНД#############################
"""
# импортируем функцию seasonal_decompose из statsmodels
#pip install statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose

# задаем размер графика
from pylab import rcParams
rcParams['figure.figsize'] = 11, 9

# применяем функцию к данным о перевозках
decompose = seasonal_decompose(btc)
decompose.plot()

plt.show()
"""
#######################################################################
"""
alpha = 0.2

# первое значение совпадает со значением временного ряда
exp_smoothing = [btc[0]]

# в цикле for последовательно применяем формулу ко всем элементам ряда
for i in range(1, len(btc)):
  exp_smoothing.append(alpha * btc[i] + (1 - alpha) * exp_smoothing[i - 1])

# выведем прогнозное значение для 
print(exp_smoothing[-1])

# посмотрим на результат на графике

# зададим размер
plt.figure(figsize = (15,8))
"""
# выведем данные о рождаемости и кривую экспоненциального сглаживания
plt.plot(btc, label = 'Данные BTC', color = 'steelblue')
plt.plot(btc, label = 'Экспоненциальное сглаживание графика', color = 'orange')

# добавим легенду, ее положение на графике и размер шрифта
plt.legend(title = '', loc = 'upper left', fontsize = 14)

# добавим подписи к осям и заголовки
plt.ylabel('1', fontsize = 14)
plt.xlabel('2', fontsize = 14)
plt.title('3', fontsize = 16)

plt.show()



# разобьём данные на обучающую и тестовую выборки

# обучающая выборка будет включать данные до декабря 1959 года включительно
btc = btc[:'2023-01']

# тестовая выборка начнется с января 1960 года (по сути, один год)
test = btc['2023-02':]
# выведем эти данные на графике
plt.plot(btc, color = "black")
plt.plot(test, color = "red")

# заголовок и подписи к осям
plt.title('Разделение данных ')
plt.ylabel('Количество ')
plt.xlabel('Месяцы')

# добавим сетку
plt.grid()

plt.show()


# принудительно отключим предупреждения системы
import warnings
warnings.simplefilter(action = 'ignore', category = Warning)

# обучим модель с соответствующими параметрами, SARIMAX(3, 0, 0)x(0, 1, 0, 12)

# импортируем класс модели
from statsmodels.tsa.statespace.sarimax import SARIMAX

# создадим объект этой модели
model = SARIMAX(btc, 
                order = (3, 0, 0), 
                seasonal_order = (0, 1, 0, 12))

# применим метод fit
result = model.fit()
# мы можем посмотреть результат с помощью метода summary()
print(result.summary())

# тестовый прогнозный период начнется с конца обучающего периода
start = len(btc)

# и закончится в конце тестового
end = len(btc) + len(test) - 1
  
# применим метод predict
predictions = result.predict(start, end)
print(predictions)

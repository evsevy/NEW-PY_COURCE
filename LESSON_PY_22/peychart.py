from pyecharts import Line
attr =["Shirt", "T-Shirt", "Jeans", "Kurtas", "Salvar", "Shoes"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
line =Line("Pacing chart for Shop A and Shop B","X-axis-->Cloths, Y-axis-->Pricing")
line.add("Shop A", attr, v1, mark_point=["average"])
line.add("Shop B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.render('poly_line.html')


from pyecharts import Pie
pie =Pie("Pie illustration example", title_pos='center', width=1000, height=600)
pie.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148], radius=[40, 55],is_label_show=True)
pie.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30], legend_orient='vertical', legend_pos='left')
pie.render('nested pie.html')


from pyecharts import Bar
Bar = Bar("Months Vs Sales of Car", "Various Manufactures")
Bar.add("Mahindra", ['MAY','JUNE','JUL','AUG'], [45,38,20,50], IS_MORE_UTILS = True)
Bar.add("Tata", ['MAY','JUNE','JUL','AUG'], [40,48,38,50], IS_MORE_UTILS = True)
Bar.add("Kia", ['MAY','JUNE','JUL','AUG'], [50,42,15,20], IS_MORE_UTILS = True)
Bar.render('bar.html') # Generates a Bar.html file in the specified directory

import plotly.express as px
stockDFclone['Date2'] = stockDFclone['Date'].apply(lambda x : x.strftime("%Y-%B-%d"))
fig = px.histogram(stockDFclone, x="Date2", y="Volume",
             color='stock_ticker', barmode='group',histfunc=None,
             height=400)
fig.update_yaxes(title_text='Volume')
fig.show()

import matplotlib.pyplot as plt
import seaborn as sns
stockDFclone = stockDF.reset_index()
sns.barplot(x = "Date", y = "Volume", hue = "stock_ticker", data = stockDFclone)
plt.show()


from datetime import datetime
from datetime import timedelta
import pandas_datareader as data_reader
import pandas as pd
stocktickers = ['GOOG', 'AAPL', 'FB']
stock = []
#Извлечение данных за 14 дней
start = (datetime.now()-timedelta(days=14)).strftime('%Y-%m-%d')
end = (datetime.now()).strftime('%Y-%m-%d')
for stockticker in stocktickers:
    data = data_reader.DataReader(stockticker, 'yahoo', start, end)
    data['stock_ticker'] = stockticker
    stock.append(data)
stockDF = pd.concat(stock)



from pyecharts.charts import Bar
from pyecharts import options as opts
date = stockDF.index.unique().tolist()
datedata = [x.strftime("%Y-%m-%d") for x in date]
GOOG = stockDF[stockDF['stock_ticker']=='GOOG']['Volume'].tolist()
AAPL = stockDF[stockDF['stock_ticker']=='AAPL']['Volume'].tolist()
FB = stockDF[stockDF['stock_ticker']=='FB']['Volume'].tolist()
bar = (Bar()
       .add_xaxis(date)
       .add_yaxis('GOOG', GOOG)
       .add_yaxis('AAPL', AAPL)
       .add_yaxis('FB', FB)
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="Maximum "),
                                                                opts.MarkPointItem(type_="min", name="Minimum")]))
       .set_global_opts(title_opts=opts.TitleOpts(title="Stock Market", subtitle="Daily Volume"),
                                       datazoom_opts=opts.DataZoomOpts(range_start=0, range_end=100),
                                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
)
       )
bar.render_notebook()

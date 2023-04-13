#https://github.com/ourownstory/neural_prophet
#pip install neuralprophet
#https://colab.research.google.com/github/ourownstory/neural_prophet/blob/main/docs/source/new-tutorials/tutorial01.ipynb

from neuralprophet import NeuralProphet
import pandas as pd

df = pd.read_csv('toiletpaper_daily_sales.csv')

m = NeuralProphet()

metrics = m.fit(df, freq="D")

forecast = m.predict(df)

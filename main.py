import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web


style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.date(2022,4,1)
df = web.DataReader('NVDA','yahoo',start,end)
print(df.head())

import pandas as pd
import pyfolio as pf
import yfinance as yf

cartera = ['YPF','GGAL','AMZN','AAPL','TLT','SHY','IEF']
data = pd.DataFrame(columns=cartera)

for ticker in cartera:
 data[ticker] = yf .download(ticker, period='10y')['Adj Close']

data = data.pct_change().dropna().mean(axis=1)


pf.create_full_tear_sheet(data)

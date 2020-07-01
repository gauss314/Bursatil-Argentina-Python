import pandas as pd
import yfinance as yf

tickers = ["BMA","BBAR","CRESY","EDN","GGAL","PAM","TEO","TGS","YPF"]

df = pd.DataFrame(index=tickers)
for ticker in tickers:
    dataDaily =  yf.download(ticker, interval="1d")['Adj Close']
    dataResample = dataDaily.resample('2Q', closed='left').last().pct_change().dropna()*100
    dataResample = dataResample.reset_index()
    dataResample.columns = ['Cierre','Yield']
    sem1 = dataResample.loc[::2]
    sem2 = dataResample.loc[1:len(dataResample)-2:2]

    df.loc[ticker,'1° Semestre Media'] = round(sem1.Yield.mean(),2)
    df.loc[ticker,'1° Semestre STD'] = round(sem1.Yield.std(),2)
    df.loc[ticker,'2° Semestre Media'] = round(sem2.Yield.mean(),2)
    df.loc[ticker,'2° Semestre STD'] = round(sem2.Yield.std(),2)

print(df, '\n\n', df.mean())








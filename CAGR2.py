import pandas as pd
import datetime as dt
import yfinance as yf

'''
Compara el yield buy & hold de cartera vs rotar 5 mejores o 5 peores de semana anterior
'''
años = 10
start = dt.date.today()-dt.timedelta(365*años)
end = dt.date.today()
tickers = ["GGAL", "BMA", "YPF", "PAM", "TGS", "CRESY", "IRS", "TEO", "MELI", "EDN", "BBAR", "TX"]
data =  yf.download(tickers, start=start, end=end, interval="1wk")['Adj Close']
yields = data.pct_change()
yields['yield']=yields.mean(axis=1)
yieldsPast = yields.shift()

best, worst = pd.DataFrame(), pd.DataFrame()
for idx, row in yieldsPast.iterrows():
    ordenadas = row.sort_values()
    best5_tickers = list(ordenadas.index[-6:-1])
    worst5_tickers = list(ordenadas.index[0:5])
    week = yields.loc[yields.index==idx]
    weekBest = week.transpose().loc[best5_tickers]
    weekWorst = week.transpose().loc[worst5_tickers]
    worst = pd.concat([worst, weekWorst],axis=1)
    best = pd.concat([best, weekBest],axis=1)

best = best.transpose()
worst = worst.transpose()
best['yield']=best.mean(axis=1)
worst['yield']=worst.mean(axis=1)

results = pd.DataFrame()
results.loc['Buy & Hold','CAGR'] = (yields['yield']+1).prod()**(1/años)-1
results.loc['Best 5 Portfolio','CAGR'] = (best['yield']+1).prod()**(1/años)-1
results.loc['Worst 5 Portfolio','CAGR'] = (worst['yield']+1).prod()**(1/años)-1

print(results.round(2))

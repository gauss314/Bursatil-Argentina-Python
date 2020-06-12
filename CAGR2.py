import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use('dark_background')

'''
Compara el yield buy & hold de cartera vs rotar 5 mejores o 5 peores de semana anterior
'''

años = 11
start = dt.date.today()-dt.timedelta(365*años)
end = dt.date.today()

tickers = ["GGAL", "BMA", "YPF", "PAM", "TGS", "CRESY", "IRS", "TEO", "MELI", "EDN", "BBAR", "CEPU", "TX", "SUPV", "LOMA"]
tickersUSA = ["AAPL", "AMZN", "NFLX", "FB", "KO", "GE", "V", "JPM", "SPY", "XOM", "TSLA", "VZ",'BAC','BABA']


data =  yf.download(tickers, start=start, end=end, interval="1wk")['Adj Close']
yields = data.pct_change()
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
yields['yield']=yields.mean(axis=1)

results = pd.DataFrame()
results.loc['Buy & Hold','CAGR'] = (yields['yield']+1).prod()**(1/10)-1
results.loc['Best 5 Portfolio','CAGR'] = (best['yield']+1).prod()**(1/10)-1
results.loc['Worst 5 Portfolio','CAGR'] = (worst['yield']+1).prod()**(1/10)-1

best['yieldAcum'] = (best['yield']+1).cumprod()-1
worst['yieldAcum'] = (worst['yield']+1).cumprod()-1
yields['yieldAcum'] = (yields['yield']+1).cumprod()-1

fig, ax = plt.subplots(figsize=(14,7))
ax.plot(yields.yieldAcum,  lw=1, c='tab:blue', label='Buy&Hold')
ax.plot(best.yieldAcum, lw=1, c='tab:green', label='Rolling Best5 previous yield week return')
ax.plot(worst.yieldAcum,  lw=1, c='tab:red', label='Rolling Worst5 previous yield week return')
plt.suptitle('Compare Buy&Hold vs Active Portfolio', y=0.95, fontsize=16)
plt.legend(fontsize=14)

columns = 3
rows = años//columns+1
fig2, ax2 = plt.subplots(figsize=(14,4*rows),nrows=rows, ncols=columns)
for i in range(años+1):
    dtFrom = dt.datetime(end.year-años +i , 1 , 1)
    dtTo = dt.datetime(end.year-años +i +1 , 1 , 1)
    yieldsYr = (yields.loc[(yields.index > dtFrom)&(yields.index < dtTo)]).copy()
    bestYr = (best.loc[(best.index > dtFrom)&(best.index < dtTo)]).copy()
    worstYr = (worst.loc[(worst.index > dtFrom)&(worst.index < dtTo)]).copy()
    bestYr['yieldAcum'] = (bestYr['yield']+1).cumprod()-1
    worstYr['yieldAcum'] = (worstYr['yield']+1).cumprod()-1
    yieldsYr['yieldAcum'] = (yieldsYr['yield']+1).cumprod()-1    
    row = i//columns
    col = i%columns
    ax2[row][col].plot(yieldsYr.yieldAcum,  lw=1, c='tab:blue')
    ax2[row][col].plot(bestYr.yieldAcum,  lw=1, c='tab:green')
    ax2[row][col].plot(worstYr.yieldAcum,  lw=1, c='tab:red')
    ax2[row][col].set_title(str(end.year-años +i), y=0.83, fontsize=20, alpha=0.4)
    plt.setp(ax2[row][col].get_xticklabels(), visible=False)    
print(results)

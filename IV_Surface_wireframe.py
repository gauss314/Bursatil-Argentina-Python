import requests, numpy as np, pandas as pd, matplotlib.pyplot as plt
from scipy import interpolate

#saquen su API key en https://developer.tdameritrade.com/content/getting-started
c_key = 'ZUHAWUVPFB5RSDODLQS08EN8EOQN5TKO'


def options(symbol):
    params = {'apikey' : c_key, 'symbol':symbol}
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/chains'
    r = requests.get(url=endpoint ,params=params)
    return r.json()


def optionsDF(chain, k_min=0, k_max=1000, ttm_min=10, ttm_max=700):
    v_calls = list(chain['callExpDateMap'].values())
    v_puts = list(chain['putExpDateMap'].values())
    calls, puts = [], []

    for i in range(len(v_calls)):
        v = list(v_calls[i].values())    
        for j in range(len(v)):
            calls.append(v[j][0])

    for i in range(len(v_puts)):
        v = list(v_puts[i].values())    
        for j in range(len(v)):
            puts.append(v[j][0])

    contracts = pd.concat([pd.DataFrame(calls),pd.DataFrame(puts)])
    tabla = contracts.loc[contracts.daysToExpiration>0].copy()
    tabla['ticker'] = chain['symbol']        
    df_ok = tabla.loc[(tabla['strikePrice'] > k_min) & (tabla['strikePrice'] < k_max)]
    df_ok = df_ok.loc[(df_ok['daysToExpiration'] > ttm_min) & (df_ok['daysToExpiration'] < ttm_max)]   
    return df_ok


def prepararMalla(columna, df, leg=None):
    if leg:
        df = df.loc[df['putCall']==leg].copy()
        
    df_ok = df.loc[:,['strikePrice','daysToExpiration',columna]]
    df_ok = df_ok.replace('NaN',np.nan).dropna()    
    x_q = len(df_ok['strikePrice'].unique())
    y_q = len(df_ok['daysToExpiration'].unique())
    x1 = np.linspace(df_ok['strikePrice'].min(), df_ok['strikePrice'].max(), x_q)
    y1 = np.linspace(df_ok['daysToExpiration'].min(), df_ok['daysToExpiration'].max(), y_q)
    X, Y = np.meshgrid(x1, y1)
    Z = interpolate.griddata((df_ok['strikePrice'], df_ok['daysToExpiration']), df_ok[columna], (X, Y))
    return X,Y,Z, df_ok


def grafCols(cols, leg=None):
    fig = plt.figure(figsize=(16,5))
    ax = [fig.add_subplot(1, len(cols), i+1, projection='3d') for i in range(len(cols))]
    for i in range(len(cols)):
        col = cols[i]
        df_greeks = data.copy()
        X,Y,Z,df = prepararMalla(col, df_greeks, leg=leg)    
        ax[i].plot_wireframe(X, Y, Z, color='white', lw=2)     
        ax[i].set_title(f'{col} ({leg})', fontsize=16, color='silver')
        ax[i].set_xlabel('Strikes', fontsize=16, color='w')
        ax[i].set_ylabel('TTM', fontsize=16, color='w')
        ax[i].set_zlabel(col, fontsize=16, color='w')
        ax[i].w_xaxis.set_pane_color((0,0,0,0))
        ax[i].w_yaxis.set_pane_color((0,0,0,0))
        ax[i].w_zaxis.set_pane_color((0,0,0,0))
        ax[i].set_zlabel(col)


plt.style.use('dark_background')

ticker = 'AAPL'
data = optionsDF(options(ticker), k_min=350, k_max=700, ttm_min=10, ttm_max=365)
grafCols(['delta','gamma'], 'CALL')
grafCols(['vega','theta'], 'CALL')
grafCols(['rho','volatility'], 'CALL')
grafCols(['percentChange','openInterest'], 'CALL')
grafCols(['timeValue','theoreticalOptionValue'], 'CALL')
grafCols(['timeValue','theoreticalOptionValue'], 'PUT')
plt.show()






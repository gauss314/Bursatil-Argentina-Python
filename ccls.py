import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


acciones = [ 
    ('GGAL', 'GGAL.BA', 10),
    ('YPF', 'YPFD.BA', 1),
    ('PAM', 'PAMP.BA', 25),
]

adrs = pd.DataFrame() 
locales = pd.DataFrame() 
ccls = pd.DataFrame() 

for accion in acciones:
    adrs[accion[0]]=yf.download(accion[0], period='1d' , interval='2m')['Adj Close']
    locales[accion[1]]=yf.download(accion[1], period='1d' , interval='2m')['Adj Close']
    ccls[accion[0]]=locales[accion[1]] * accion[2] / adrs[accion[0]]
    ccls[accion[0]].interpolate(method='linear',inplace=True)


print(ccls.tail())



plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [15, 6]
ccls.plot()
plt.show()


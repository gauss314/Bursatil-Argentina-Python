import matplotlib.pyplot as plt, numpy as np
from alpha_vantage.timeseries import TimeSeries as seriesAlpha

ticker = "GGAL"
serie = seriesAlpha(key='IUIHYQWABRBAMCH6', output_format='pandas')
data, metadata = serie.get_intraday(symbol=ticker,interval='1min', outputsize='full')
data.columns = ['Open','High','Low','Close','Volume']

n = 16 # filas y cols de la matriz de rangos nxn 
quantiles = [i/n for i in range(n)]
precios = list(data.quantile(quantiles).Close.round(2))
volumenes = list(data.quantile(quantiles).Volume.round(2))

x = precios*n
y=[]
for volumen in volumenes:
    for j in range(n):
        y.append(volumen)

cantidades = [0 for i in range(100)]
data['vRank'] = (data.Volume.rank(pct=True)*n).apply(np.ceil)
data['pRank'] = (data.Close.rank(pct=True)*n).apply(np.ceil)
data['orden'] = (data.vRank-1)*n+data.pRank-1

dx = (data.Close.max()-data.Close.min())*(1/n)*0.05
dy = (data.Volume.mean())*(1/n)*0.1
dz = (data.groupby('orden').Volume.count())

        
plt.style.use('dark_background')
fig = plt.figure(figsize=(14, 7.8))
ax1 = fig.add_subplot(projection='3d')
ax1.bar3d(x, y, 0, dx, dy, list(dz), color='gray')

for a,b,c in zip(x,y,list(dz)):
    ax1.plot(x,y,dz, "o", markersize=4, color='red')

ax1.set_title('Perfil Precio/Vol en velas de 1 minunto -- '+ticker, color='silver', fontsize=20, y=0.85)
ax1.xaxis.pane.fill = ax1.yaxis.pane.fill = ax1.zaxis.pane.fill = False
ax1.grid(False)

ax1.set_xlabel('Precio', fontsize=14)
ax1.set_ylabel('Volumen', fontsize=14)
ax1.set_zlabel('Cantidad Operaciones', fontsize=14)
ax1.xaxis.pane.set_edgecolor('k')
ax1.yaxis.pane.set_edgecolor('k')
ax1.zaxis.pane.set_edgecolor('k')
plt.show()

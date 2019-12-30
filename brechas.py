import yfinance as yf
import pandas as pd

tickers=["ARS=X","AY24.BA","AY24D.BA","AO20.BA","AO20D.BA",'GGAL.BA','GGAL',"YPFD.BA","YPF","PAMP.BA","PAM",]
data=pd.DataFrame(columns=tickers)

for ticker in tickers:
    data[ticker]=yf.download(ticker, period='2d' , interval='5m')['Adj Close']

#Esta linea es para cuando hay datos en blanco que interpole y complete los datos vacios
#Es muy util cuando se usan cocientes entre series temporales que operan distintos horarios
data.interpolate(method='linear',inplace=True)

#Primero defino tablas a llenar, una para los tipos de dolar y otra para las brechas
dolares=pd.DataFrame()
brechas=pd.DataFrame()

#Voy armando la tabla con los ditintos dolares
dolares['Oficial'] = data["ARS=X"]

#Calculo del dolar CCL como el promedio del CCL de GGAL, PAM e YPF
dolares['CCL'] = data['GGAL.BA']*10 /data['GGAL']
dolares['CCL'] += data['YPFD.BA']*1/data['YPF'] 
dolares['CCL'] += data['PAMP.BA']*25/data['PAM']
dolares['CCL'] /= 3

#Calculo del dolar MEP como el promedio entre el MEP del AY24 y el AO20
dolares['MEP'] = data['AY24.BA'] /data['AY24D.BA']
dolares['MEP'] += data['AO20.BA']/data['AO20D.BA'] 
dolares['MEP'] /= 2

#Calculo de brechas oficial vs MEP y CCL
brechas['Brecha MEP %'] = (dolares['MEP'] / dolares['Oficial'] - 1)*100
brechas['Brecha CCL %'] = (dolares['CCL'] / dolares['Oficial'] - 1)*100

#Diferencia entre brecha CCL y brecha MEP
brechas['CCL-MEP'] = brechas['Brecha CCL %'] - brechas['Brecha MEP %']


print(dolares.tail())
print('\n\n')
print(brechas.tail())



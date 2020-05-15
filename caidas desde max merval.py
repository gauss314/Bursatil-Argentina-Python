import yfinance as yf
import pandas as pd

años = 10
ruedas = 100  # La cantidad de ruedas para filtrar por volumen operado
cantidadAcciones = 45 # Las acciones de mayor volumen ultimas ruedas para mostrar 

ccl = pd.DataFrame()
adr = yf.download("YPF", period= str(años)+'Y' , interval='1d')['Adj Close']
local = yf.download("YPFD.BA", period=str(años)+'Y' , interval='1d')['Adj Close']
ccl = (local / adr).to_frame()
ccl.columns = ['CCL']

tickers = ['AGRO.BA','ALUA.BA','AUSO.BA','BBAR.BA','BHIP.BA','BMA.BA','BOLT.BA','BPAT.BA','BRIO.BA',
           'BYMA.BA','CADO.BA','CAPX.BA','CARC.BA','CECO2.BA','CELU.BA','CEPU.BA','CGPA2.BA','COME.BA',
           'CRES.BA','CTIO.BA','CVH.BA','DGCU2.BA','EDN.BA','ESME.BA','FERR.BA','GAMI.BA','GARO.BA',
           'GCLA.BA','GGAL.BA','GRIM.BA','HARG.BA','HAVA.BA','INAG.BA','INTR.BA','INVJ.BA','IRCP.BA',
           'IRSA.BA','LOMA.BA','LEDE.BA','LONG.BA','METR.BA','MIRG.BA','MOLA.BA','MOLI.BA','MORI.BA',
           'OEST.BA','PAMP.BA','PATA.BA','PGR.BA','RICH.BA','ROSE.BA','SAMI.BA','SEMI.BA','SUPV.BA',
           'TECO2.BA','TGNO4.BA','TGSU2.BA','TRAN.BA','TXAR.BA','YPFD.BA']

data = yf.download(tickers, period=str(años)+'Y' , interval='1d')
vol = (data['Close']*data['Volume'] /1000000).rolling(ruedas).mean().tail(1).squeeze()
tickers = list(vol.sort_values(ascending=False).head(cantidadAcciones).index)

data = yf.download(tickers, period=str(años)+'Y' , interval='1d')['Adj Close'].abs()
dataCCL = data.div(ccl.CCL, axis=0)

fechasMax = dataCCL.idxmax()
preciosMax = dataCCL.max()
fechasMin = dataCCL.idxmin()
preciosHoy = dataCCL.tail(1).squeeze()
upside = ((preciosMax/preciosHoy-1)*100)
desdeMax = ((preciosHoy/preciosMax-1)*100)

tabla = pd.concat([fechasMax,fechasMin,preciosMax,preciosHoy,desdeMax,upside], axis=1)
tabla.columns = ['Fecha Px Max','Fecha Px Min','Px Max','Px Hoy','DesdeMax','HastaMax']
tabla = tabla.sort_values('HastaMax', ascending=False).round(2)

print('\n',tabla)

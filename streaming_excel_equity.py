import xlwings as xw, websocket as ws
import json, time, pandas as pd

token = 'a5e16af3958b5c8d88d63c84fb9fc9f0d1be4434'
# Sacar el api key gratuito propio en https://api.tiingo.com/

wb = xw.Book('streaming_excel_eq.xlsx')  
# Este archivo debe existir en el mismo directorio donde se ejecuta este script, puede ser un excel en blanco pero con ese nombre


hoja = wb.sheets('Eq')

tickers = ['GM','GE','BAC','INTC','AMD','KO','EBAY','VALE','F','T','VZ','HPQ','BKR','PFE']
# La lista de tickers de puede cambiara gusto con acciones de USA, funciona en horario de mercado



def changeColor(ticker):
    num = tickers.index(ticker) + 5
    string = 'B'+str(num)+':H'+str(num)
    hoja.range(string).color = xw.utils.rgb_to_int((220, 220, 220))
    time.sleep(0.005)
    hoja.range(string).color = xw.utils.rgb_to_int((255, 255, 255))
    
    
filas = {}
for i in range(len(tickers)):
    filas[tickers[i]] = i+5

celdas = {}
for ticker,numero in filas.items():
    celdas[ticker] = {'ticker':'B' + str(numero), 'precio': 'C' + str(numero),
        'bid_q':  'D' + str(numero), 'bid':  'E' + str(numero), 'ask':  'F' + str(numero), 
        'ask_q':  'G' + str(numero),'time':  'H' + str(numero) } 
    
conn = ws.create_connection("wss://api.tiingo.com/iex")
subscribe = '{"eventName":"subscribe","authorization":"'+token+'","eventData":{"thresholdLevel":5}}'
conn.send(subscribe)
subscription =  json.loads(conn.recv())
subscriptionId = subscription['data']['subscriptionId']
inicio_recepcion = json.loads(conn.recv())

while True:
    try:
        result =  json.loads(conn.recv())['data']
        ticker = result[3].upper()
        changeColor(ticker)
        if ticker in tickers:
            print('Actualizado:',ticker)
            hoja.range(celdas[ticker]['ticker']).value = ticker            
            hoja.range(celdas[ticker]['time']).value = pd.to_datetime(result[1]).ctime()
            if result[0]=='Q':
                hoja.range(celdas[ticker]['bid_q']).value = result[4]
                hoja.range(celdas[ticker]['bid']).value = result[5]
                hoja.range(celdas[ticker]['ask']).value = result[7]
                hoja.range(celdas[ticker]['ask_q']).value = result[8]
            else:
                hoja.range(celdas[ticker]['precio']).value = result[9]
    except:
        pass        



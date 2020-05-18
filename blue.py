import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

def scrap(año, mes):
    url  = 'https://www.cotizacion-dolar.com.ar/dolar-blue-historico-'+str(año)+'.php'
    for i in range(1,7):
        try:        
            fecha = datetime.datetime(año,mes,i)
            data = {'fecha': fecha.strftime('%d-%m-%y')}
            resp = requests.post(url, data=data)
            soup = BeautifulSoup(resp.text, "html.parser")
            break
        except:
            print('Falló en ',i)    
    filas = soup.find_all('td', {'style' : 'padding: 1%'})
    return filas

def parsear(filas):
    mensual = pd.DataFrame() 
    for i in range(1, int(len(list(filas))/3)):
        dic = {}
        dic['fecha'] = filas[3*i].text
        dic['bid'] = filas[3*i+1].text
        dic['ask'] = filas[3*i+2].text
        rueda = pd.DataFrame.from_dict(dic, orient='index').transpose().set_index('fecha')
        rueda.index = pd.to_datetime(rueda.index)
        mensual = pd.concat([mensual,rueda], axis=0)
    return mensual

def downloadAño(año):
    tablaAnual = pd.DataFrame()
    for i in range(1,13):
        filas = scrap(año=año, mes=i)
        tabla = parsear(filas)
        tablaAnual = pd.concat([tablaAnual,tabla],axis=0)
        print('mes',i,'listo')        
    tablaAnual.to_excel('blue_'+str(año)+'.xlsx')
    print(tablaAnual)

downloadAño(2016)

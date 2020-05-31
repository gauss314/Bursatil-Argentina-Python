# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:30:23 2019

@author: Sergio
"""

#Importar librerías de yfinance
import yfinance as yf
ticker = "GGAL.BA"
data = yf .download(ticker, period='2y')
#
#
data['Non_trading_gap'] = data.Open - data.Close.shift(-1)
# Construye nueva columna con Ganancia en tiempo no No Operable
data['Trading_sigma'] = data.High - data.Low
# Construye columna con datos de la volatilidad diaria
#Esta es la máxima valuación positiva de rango para el día. Siempre
data['Trading_today_earning'] = data.Close - data.Open
# Construye columna con ganancia/pérdida en tiempo de operatoria
print(data.head(4))
print('\n--Describe--\n', data.describe())
print('\n--Columns--\n', data.columns)


print('\n--Gráfico con Ganancia en NON Trading Hours versus Ganancia en trading hours--')
import matplotlib.pyplot as plt
plt .style.use('dark_background')
plt.rcParams['figure.figsize'] = [12.0, 5]

data['Non_trading_gap'].plot(kind='line',title='Gap diario comparando Operatoria diaria')
data['Trading_today_earning'].plot(kind='line',title='Gap diario comparando Operatoria diaria')    

'''
HOMEWORK - Tareas para el hogar
Buscar y encontrar relaciones (en realidad es evidente) entre la operatoria
diaria y la NO OPERATORIA NOCTURNA
Analizar la serie de datos y evaluar la correlación.
Genera una oportunidad de ir en contra tendencia según muestre la no operatoria 
previa luego del arranque (Open) para operar durante el día.
Analizar y comentar
'''

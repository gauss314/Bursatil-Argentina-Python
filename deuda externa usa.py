import matplotlib.pyplot as plt
import requests, pandas as pd



def deuda(limit=10000):
    
    # Preparo el request
    base = 'https://www.transparency.treasury.gov/services/api/fiscal_service/v1/'
    url = base + 'accounting/od/debt_to_penny'
    params = {'sort':'-data_date', 'limit':limit}
    
    # Hago el request y lo paso a un DataFrame
    r = requests.get(url, params=params)
    js = r.json()
    df = pd.DataFrame(js['data'])
    
    # Tomo solo las columnas que necesito
    df = df.iloc[:,[0,1,2,3]]
    
    # Renombro las columnas
    df.columns = ['fecha','Externa','Intragov','Deuda Total']
    
    # Seteo el indice
    df.set_index('fecha', inplace=True)
    
    # Paso el índice a formato datetime
    df.index = pd.to_datetime(df.index)
    
    # Transformo a numerico los valores de las columnas de deuda
    df = df.apply(pd.to_numeric)
    
    return df   

deuda = deuda()
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(deuda)
ax.legend(labels=deuda.columns, loc='upper left', fontsize=14)
fig.suptitle('Deuda Externa USA', y=0.95, fontsize=16)
plt.show()




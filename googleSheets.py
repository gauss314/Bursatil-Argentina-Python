import pandas as pd

# Vamos a leer los datos de la hoja de googleShets: 
# https://docs.google.com/spreadsheets/d/1AuPacbaub5KK6piq75ETSAqnFhIjU1XN9pQh8SJu3mI/edit#gid=1254736984


url = 'https://docs.google.com/spreadsheets/d/'

# Esta en la URL de la planilla despues de la url de la linea anterior 
token = '1AuPacbaub5KK6piq75ETSAqnFhIjU1XN9pQh8SJu3mI' 

# gid está en la url de la planilla figura como gid=... 
#Es el ID de la Hoja dentro de la planilla
gid = '1254736984'

# Leo la planilla y ya, salteo 1 fila en este caso
r = pd.read_csv(url + token + '/export?gid='+gid+'&format=csv', skiprows=1)
print('Tabla de la Hoja de Históricos\n',r)



# Aca leo la Hoja de precios
gid = '0'       # ID de la hoja (está en la URL)
row_from = 4    # desde que fila quiero
row_to = 8      # Hasta que fila quiero
cols=['Ticker','Last','TradeTime']  # Que columnas quiero de la tabla


rows = list(range(row_from-1,row_to))
r = pd.read_csv(urlGoogle + token + '/export?gid='+gid+'&format=csv',
                usecols=cols, skiprows = lambda x: x not in rows)

print('Tabla de la Hoja de Precios\n', r)

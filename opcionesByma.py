import pandas as pd
url = 'http://www.rava.com/precios/panel.php?m=OPC'

# Esta linea lee a url, el [8] es porque es la 8va tabla de la pagina la que tiene las opciones
df = pd.read_html(url, thousands='.')[8]

# Esta linea le pone como nombres de columnas los valores que estaban en la primera fila
df.columns = list(df.loc[0,:])

# Esta linea elimina la primera fila que estaba con nombres de columnas
df = df.drop(0,axis=0)

# Esta linea remplaza las comas por puntos ya que pandas transforma a numero los flotantes con punto no con coma
df = df.replace(',','.',regex=True)

# Esta linea transforma a numero las columnas de 1 a 7 y redondea a 2 decimales
df[df.columns[1:7]] = df[df.columns[1:7]].apply(pd. to_numeric, errors='coerce').round(2)

# Esta Línea hace lo propio con las dos ultimas pero  como son enteros no hace falta redondear
df[df.columns[8:10]] = df[df.columns[8:10]].apply(pd. to_numeric, errors='coerce')

# #Lo guardo en un excel
df. to_excel('opciones.xlsx')

# Imprimo el DataFrame
print(df)

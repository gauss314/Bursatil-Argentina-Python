import pandas as pd
import requests
from bs4 import BeautifulSoup
from IPython.display import HTML

def extraer_texto(texto, start_marker, end_marker):
    try:
        start = texto.index(start_marker) + len(start_marker)
        end = texto.index(end_marker, start)
    except ValueError as e:
        print(f"Error: {e}")
        return 
    
    return texto[start:end]


url = 'https://www.rava.com/cotizaciones/opciones'
find = 'opciones-p'
find_also = "body"

""""
url = 'https://www.rava.com/cotizaciones/cedears'
find = 'cedears-p'
find_also = "body"

url = 'https://www.rava.com/cotizaciones/bonos'
find = 'bonos-p'
find_also = "body"

url = 'https://www.rava.com/cotizaciones/futuros'
find = 'futuros-p'
find_also = "ROFEX"

url = 'https://www.rava.com/cotizaciones/acciones-argentinas'
find = 'acciones-argentinas'
find_also = "GEN" # "GEN" o "LID"
"""

# Obtiene datos url
try: 
    res = requests.get(url, timeout=10)
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

soup = BeautifulSoup(res.content, "lxml")

# Extrae info opciones
opciones = extraer_texto(soup.__str__(), '<' + find  +' :', '</' + find +'>' )
opciones = (extraer_texto(opciones, '"'+ find_also + '":', '}],') + '}')[1:]

# Crea df con los datos
df = pd.read_json('[' + opciones + ']', orient='records')

if find == 'acciones-argentinas':
    opciones = extraer_texto(soup.__str__(), '<' + find  +' :', '</' + find +'>' )
    find_also = "LID"
    opciones = opciones[opciones.rfind(find_also)-1:]
    opciones = (extraer_texto(opciones, '"'+ find_also + '":', '}]') + '}')[1:]
    df1 = pd.read_json('[' + opciones + ']', orient='records')
    df = pd.concat([df1, df], ignore_index=True)

df = df.fillna("")


# Lo guardo en un excel
df. to_excel('opciones.xlsx')

# Imprimo el DataFrame
print(df)

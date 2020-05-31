import pandas as pd
url = 'http://www.rava.com/precios/panel.php?m=OPC'
df = pd.read_html(url, thousands='.')[8]
df.columns = list(df.loc[0,:])
df = df.drop(0,axis=0)
df = df.replace(',','.',regex=True)

df[df.columns[1:7]] = df[df.columns[1:7]].apply(pd. to_numeric, errors='coerce').round(2)
df[df.columns[8:10]] = df[df.columns[8:10]].apply(pd. to_numeric, errors='coerce')
df. to_excel('opciones.xlsx')

print(df)
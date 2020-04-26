import pandas as pd, matplotlib.pyplot as plt

# Extraccion de subtitulos y conteo de palabras
def getData(videoID):
    from youtube_transcript_api import YouTubeTranscriptApi    
    data = YouTubeTranscriptApi.get_transcript(videoID, languages=['es'])
    df = pd.DataFrame(data)
    compList = list(df['text'].str.split(" "))
    flatList = [item for sublist in compList for item in sublist]
    wordsDF = pd.DataFrame(flatList, columns=['words'])
    conteo = wordsDF.words.value_counts().to_frame()
    return conteo

# Filtro de palabras sin significado propio
def filterDataEsp(df):
    filt = 'que de la y en el a los un es las se por lo con del nos una como al'
    filt += ' más esto este está al eso hay ha su les porque esta son cada sin me'
    filt += ' sus ser ese cómo han qué acá estas allí va ahí mi aquí o le esa para'
    filtList = filt.split()
    ret = df[~df.index.isin(filtList)]
    return ret

# Gráfico Top N
def graf(df, n=30):
    top = dataF.head(n)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15,5))
    ax.bar(top.index, top.words, color='tab:blue')
    plt.xticks(rotation=90, fontsize=18)
    return plt

videoID = 'zXfNnB7fjVo' # 25 Abr 2020 Cadena Nac AF
top = 40

# Recoleccion de datos, filtrado y grafico en pantalla
data = getData(videoID)
dataF = filterDataEsp(data)
graf(dataF, top).show()

# Ipmprimir diccionario top 200
dataDict={}
for idx, row in dataF.head(200).iterrows():
    dataDict[idx]=row.words
print(dataDict)

#Comparar Palabras
f = dataF[dataF.index.isin(['yo','nosotros','ustedes'])]
print(f)


# Instalar el paquete YouTubeTranscriptApi:
# pip install youtube_transcript_api
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Parametrización
papel = "YPF" # Disponibles: XOM RDSa BP PAM YPF CVX COP EOG SLB VLO WMB
n = 10 # Cantidad de Clusters: Cualquier valor entero de 2 a 10
mCorr= "pearson" # pearson, spearman, kendall (son métodos de regresión)

# Detalles del Gráfico
plt.style.use('dark_background')
plt.figure(figsize=(12,6))
colores= ["orange","green","brown","cyan","magenta","blue","red","yellow","lightgreen","pink"]  
plt.title('Clusterización (n=' +str(n)+ ') de correlacíón (' + mCorr + ') WTI-'+papel, fontsize=18)
plt.xlabel('WTI USD', fontsize=14)
plt.ylabel(papel+' USD', fontsize=14)

# Lectura de Datos
data = pd.read_excel("Oil.xlsx")
Px = np.array(list(zip(data['WTI Px'], data[papel + " Px"])))
Var = np.array(list(zip(data['WTI Var'], data[papel + " Var"])))
print("\n\nCorrelación",papel,"R^2 =",data['WTI Var'].corr(data[papel+' Var'],method=mCorr).round(4))

# Algo de Clusterizacion
km = KMeans(n_clusters=n, n_init=15, max_iter=300, algorithm="elkan")
y_means = km.fit_predict(Px)

clustersList = list(y_means)
for i in range(len(data)):
    data.loc[i,'cluster'] = clustersList.pop()

for c in range(n):
    df = data.loc[data.cluster == c]
    co = round(df['WTI Var'].corr(df[papel + " Var"], method=mCorr),2)
    plt.scatter(Px[y_means==c,0],Px[y_means==c,1], s=1, color=colores[c])
    coords = (km.cluster_centers_[c,0] - data['WTI Px'].mean()*0.1, km.cluster_centers_[c,1])
    plt.gca().annotate("R^2 ="+str(co), coords, fontsize=18, c="w")

plt.show()

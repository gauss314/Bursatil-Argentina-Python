import random, json, pandas as pd
import matplotlib.pyplot as plt, matplotlib.ticker as ticker

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12,12))

mu = 0.04  # media diaria del pct_change
sigma = 2 # Volatilidad diaria del pct_change
ruedas = 250
simulaciones = 1000

capital = [[100] for i in range(simulaciones)]

for j in range(simulaciones):
    for i in range(ruedas):
        v = random.normalvariate(mu,sigma)
        capital[j].append(capital[j][i] * (1+v/100))
    ax.plot(capital[j], lw=1, alpha=1 )

ax.set_yscale('log')
ax.set_xlabel('Ruedas', fontsize=15, color='silver')
ax.set_ylabel('Capital', fontsize=15, color='silver')
ax.set_yticks([60, 100, 200])
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))

fig.suptitle(f'Montecarlo básico cartera mu diario={mu}, sigma diario={sigma}',
             y=0.17, fontsize=18, color='silver')
plt.show()

df = pd.DataFrame(capital).round(2)
resumen = {}
resumen['minTemporal'] = df.min().min()
resumen['maxTemporal'] = df.max().max()
resumen['minFinal'] = df.transpose().iloc[-1:].squeeze().min()
resumen['maxFinal'] = df.transpose().iloc[-1:].squeeze().max()
resumen['medio'] = round(df.transpose().iloc[-1:].squeeze().mean(),2)
resumen['errorAbsMedia'] = round(resumen['medio'] * 1/(simulaciones**0.5),2)
print(json.dumps(resumen, indent=5))








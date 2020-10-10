import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

tickers =['GGAL','GGAL.BA','YPF','YPFD.BA','PAM','PAMP.BA']
data = yf.download(tickers, auto_adjust=True, start='2011-01-01')['Close']
print('\n\n')

ccl = data['YPFD.BA']/data['YPF']
ccl += data['GGAL.BA']/data['GGAL'] * 10
ccl += data['PAMP.BA']/data['PAM'] * 25
ccl /= 3

ruedas = 55
subas_fw = ccl.pct_change(ruedas)*100
fig, ax = plt.subplots(figsize=(15,10), nrows=2)

ax[0].hist(subas_fw, bins=150, width=0.2, color='w', alpha=0.4)
ax[0].set_title(f'CCL pctChange a {ruedas} Ruedas, Histograma', y=1, fontsize=16)

serie = subas_fw.rolling(20).mean()
ax[1].plot(serie, color='silver', lw=1, alpha=0.75)
ax[1].fill_between(serie.index, 0, serie, where = serie < 0 , color='red', alpha=0.2)
ax[1].fill_between(serie.index, 0, serie, where = serie > 0 , color='green', alpha=0.2)

ax[1].set_title('CCL pctChange a {ruedas}  Ruedas, SMA mensual', y=1, fontsize=16)

values = [5,10,15,20,25,30]
targets = ((1 + np.array(values)/100)*ccl.iloc[-1]).round(2)

for z in range(len(values)):
    ax[0].axvline(values[z], color='w', ls='--', lw=1, alpha=0.35)
    ax[1].plot(ccl.index, [values[z]]*len(ccl), 'w--', alpha=0.35)
    sup_z = len(subas_fw.loc[subas_fw > values[z] ])/len(subas_fw)
    print(f'Prob de suba {ruedas} ruedas > {values[z]}% (${targets[z]}): {round(sup_z*100,1)}%')

plt.subplots_adjust(wspace=None, hspace=0.2)
plt.show()

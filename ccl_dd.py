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

ccl_max_h = ccl.cummax()
ccl_dd = ((ccl/ccl_max_h-1)*100).dropna().rolling(30).mean()

fig, ax = plt.subplots(figsize=(16,10), nrows=2)

ax[0].hist(ccl_dd, bins=150, width=0.1, color='w', alpha=0.3)
ax[0].set_title('CCL DrawDowns Histograma', y=1, fontsize=16)

ax[1].plot(ccl_dd, color='silver', lw=1)
ax[1].fill_between(ccl_dd.index, 0, ccl_dd, color='red', alpha=0.15)
ax[1].set_title('DrawDowns CCL', y=1, fontsize=16)

values = [-10,-15,-20,-25]
targets = ((1 + np.array(values)/100)*ccl.iloc[-1]).round(2)

for z in range(len(values)):
    ax[1].plot(ccl.index, [values[z]]*len(ccl), 'w--', alpha=0.5)
    sub_z = len(ccl_dd.loc[ccl_dd < values[z] ])/len(ccl_dd)
    print(f'Probabilidad de baja > {-values[z]}% (${targets[z]}): {round(sub_z*100,1)}%')

plt.subplots_adjust(wspace=None, hspace=0.2)
plt.show()

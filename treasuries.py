import matplotlib.pyplot as plt
import requests, pandas as pd

def getRates(limit):
    base = 'https://www.transparency.treasury.gov/services/api/fiscal_service/v1/'
    url = base + 'accounting/od/avg_interest_rates'
    params = {'sort':'-reporting_date', 'limit':limit}
    r = requests.get(url, params=params)
    js = r.json()
    df = pd.DataFrame(js['data'])
    return df  

data = getRates(10000)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12,6))

tipos = ['Treasury Bills','Treasury Notes','Treasury Bonds']
for tipo in tipos:
    serie = data.loc[data.security_desc==tipo]
    serie = serie.loc[:,['reporting_date','avg_interest_rate_amt']]
    serie.set_index('reporting_date', inplace=True)
    serie.index = pd.to_datetime(serie.index)
    serie.avg_interest_rate_amt = pd.to_numeric(serie.avg_interest_rate_amt)
    ax.plot(serie, label=tipo)

ax.legend(loc='upper right', fontsize=14)
plt.show()

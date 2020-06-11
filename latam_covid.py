import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12,10))

data = pd.read_excel('https://covid.ourworldindata.org/data/owid-covid-data.xlsx')

countries = ['ARG','BRA','PER','CHL','COL','MEX']
for country in countries:
    p = (data.loc[data.iso_code == country]).copy()
    p.set_index('date',inplace=True)
    p.index = pd.to_datetime(p.index)
    p.sort_index(inplace=True)
    p['pct_change'] = p.total_cases.pct_change().rolling(30).mean()
 
    if country=='ARG':
        width=5
    else:
        width=1
    ax.plot(p['pct_change'], lw=width, label=country)
    ax.legend(fontsize=14, loc='upper right')
    ax.set_xlim(dt.datetime(2020,5,1),dt.datetime.now())
    ax.set_ylim(0.02,0.09)
    

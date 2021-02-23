import requests
from bs4 import BeautifulSoup
import csv
import urllib


url = 'https://www.seraku.co.jp/service/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')


    
data = []
spots = soup.find_all('div', attrs={'class':"summary-p__name_jp"})
conts = soup.find_all('div', attrs={'class':"summary-p__txt"})

for spot, cont in zip(spots,conts ):

    
    spot_name = spot.text.replace('Dx','Dx,').replace('SI','SI,')
    cont = cont.text
    
    
    details = {}
    datum = details
    datum['サービス分野、サービス名']= spot_name
    datum['内容']= cont

    data.append(datum)
    import pandas as pd
    df = pd.DataFrame(data)
    print(df)

#保存、パスの指定

df.to_csv('./scraped-seraku-services.csv',index=False, encoding='utf_8_sig')




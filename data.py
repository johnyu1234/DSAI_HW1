import csv
import pandas as pd 
import matplotlib.pyplot as plt
import io
import requests
url = 'https://data.taipower.com.tw/opendata/apply/file/d006005/台灣電力公司_過去電力供需資訊.csv'
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))
print(df)

plt.figure(figsize=(16,5))
plt.plot(df.index,df['備轉容量(MW)'])
plt.show()
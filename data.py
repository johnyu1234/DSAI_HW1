import csv
import pandas as pd 
import io
import requests

url = 'https://data.taipower.com.tw/opendata/apply/file/d006005/台灣電力公司_過去電力供需資訊.csv'
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))
url_1 = 'https://data.taipower.com.tw/opendata/apply/file/d006002/本年度每日尖峰備轉容量率.csv'
s=requests.get(url_1).content
df_month = pd.read_csv(io.StringIO(s.decode('utf-8')))
df_month = df_month.rename(columns={'備轉容量(萬瓩)':'備轉容量(MW)'}) #change name to MW
df_month = df_month[['日期', '備轉容量(MW)']]
df_month['備轉容量(MW)'] = df_month['備轉容量(MW)'].multiply(10) # converting data to MW value
df = df[['日期', '備轉容量(MW)']]
df['日期'] = pd.to_datetime(df['日期'], format='%Y%m%d')
df.set_index('日期', inplace=True)
df_month['日期'] = pd.to_datetime(df_month['日期'], format='%Y/%m/%d')
df_month.set_index('日期', inplace=True)

df = pd.concat([df,df_month])
index = df.index
is_dupli = index.duplicated(keep="first")
not_dupli = ~is_dupli
df = df[not_dupli]
df.to_csv("training.csv")

import csv
import pandas as pd 
import matplotlib.pyplot as plt
import io
import requests
from statsmodels.tsa.arima.model import ARIMA

url = 'https://data.taipower.com.tw/opendata/apply/file/d006005/台灣電力公司_過去電力供需資訊.csv'
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))
x = df.iloc[:,0]
y = df.iloc[:,3]
j = df.iloc[:,4]
train = y[:400]
test = y[400:]
train_1 = j[:400]
test_1 = j[400:]
for i in range(24):
    model = ARIMA(train,exog=train_1,order=(5,1,0))
    model_fit = model.fit()
    # print(model_fit.summary())
    output = model_fit.forecast(exog=test_1.iloc[i])
    prediction = pd.Series(output.values)
    print(prediction[0],test.iloc[i])
    train = pd.concat([train,pd.Series(test.iloc[i])],ignore_index=True)
    train_1 = pd.concat([train_1,pd.Series(test_1.iloc[i])],ignore_index=True)
print(len(y))
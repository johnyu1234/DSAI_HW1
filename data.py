import csv
import pandas as pd 
import matplotlib.pyplot as plt
import io
import requests
from statsmodels.tsa.arima.model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np
url = 'https://data.taipower.com.tw/opendata/apply/file/d006005/台灣電力公司_過去電力供需資訊.csv'
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
def check_stationarity(ts):
    dftest = adfuller(ts)
    adf = dftest[0]
    pvalue = dftest[1]
    critical_value = dftest[4]['5%']
    if (pvalue < 0.05) and (adf < critical_value):
        print('The series is stationary')
    else:
        print('The series is NOT stationary')

x = df.iloc[:,0]
y = df.iloc[:,3]
# y = NormalizeData(y)
j = df.iloc[:,4]
train = y[:-14]
test = y[-14:]
df['日期'] = pd.to_datetime(df['日期'], format='%Y%m%d')
df.set_index('日期', inplace=True)
result = seasonal_decompose(df['備轉容量(MW)'], model='additive',extrapolate_trend='freq')
seasonal = result.seasonal

check_stationarity(df['備轉容量(MW)'])
# pacf graph
# plot_pacf(seasonal, lags =7)
# plt.show()
# # acf graph 
# plot_acf(seasonal, lags =6)
# plt.show()

model = ARIMA(train,order=(1, 1, 1) ,seasonal_order=(6,1,6,7), enforce_stationarity=False, enforce_invertibility=False)
# model = auto_arima(train,trace=True,seasonal=True,error_action='ignore', suppress_warnings=True,enforce_stationarity=False, enforce_invertibility=False)
model_fit = model.fit()
# print(model_fit.summary())
predicted = model_fit.predict(start=len(train), end=len(train)+13)

print(mean_squared_error(test,predicted,squared=False)) # RSME
plt.figure(figsize = (10,6))
plt.plot(train,label="previous data",color="blue")
plt.plot(test, label = "true values", color = "cornflowerblue")
plt.plot(predicted,label = "forecasts", color='darkorange')
plt.title("ARIMA Model", size = 14)
plt.show()


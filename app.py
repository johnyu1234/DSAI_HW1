from statsmodels.tsa.arima.model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np
import matplotlib.pyplot as plt

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


# You can write code above the if-main block.
if __name__ == '__main__':
    # You should not modify this part, but additional arguments are allowed.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')

    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.
    import pandas as pd
    df_training = pd.read_csv(args.training)
    df_training['日期'] = pd.to_datetime(df_training['日期'], format='%Y-%m-%d')
    df_training.set_index('日期', inplace=True)
    # result = seasonal_decompose(df['備轉容量(MW)'], model='additive',extrapolate_trend='freq')
    # result.plot()
    # plt.show()
    # smodel = auto_arima(train, start_p=1, start_q=1,
    #                          test='adf',
    #                          max_p=7, max_q=7, m=7,
    #                          start_P=0, seasonal=True,
    #                          d=None, D=1, trace=True,
    #                          error_action='ignore',  
    #                          suppress_warnings=True,
    #                          enforce_stationarity=False,
    #                          enforce_invertibility=False,
    #                          stepwise=True)
    # smodel.summary()
    model = ARIMA(df_training,order=(2, 0, 1) ,seasonal_order=(6,1,6,7), enforce_stationarity=False, enforce_invertibility=False)
    model_fit = model.fit()
    print(model_fit.summary())
    df_result = model_fit.predict(start='2022-03-30', end='2022-4-13')

    # conversion of series to dataframe
    df_result = pd.DataFrame(df_result).reset_index(drop=False)
    df_result.columns = ['日期','備轉容量(MW)']

    # graph drawing 
    # plt.figure(figsize = (10,6))
    # plt.plot(df_training['備轉容量(MW)'],label="previous data",color="blue")
    # plt.plot(test, label = "actual data", color = "green") 
    # plt.plot(df_result['備轉容量(MW)'],label = "prediction", color='red')
    # plt.title("ARIMA Model", size = 14)
    # plt.show()

    df_result['備轉容量(MW)'] = df_result['備轉容量(MW)'].round().astype('Int64')
    df_result['日期'] = df_result['日期'].apply(str).str.replace('-','')
    df_result['日期'] = df_result['日期'].str[:7]
    df_result.to_csv(args.output,index=False)


    # print(mean_squared_error(test,predicted,squared=False)) # RSME for evaluation of model


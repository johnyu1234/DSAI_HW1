# DSAI_HW1

Given a time series electricity data to predict the value of the operating reserve value of each day during 2022/03/30 ~ 2022/04/13. 



## Dataset Used

Dataset is extracted from [台灣電力公司](https://data.gov.tw/).  
1.台灣電力公司_過去電力供需資訊(https://data.gov.tw/dataset/19995)  
2.台灣電力公司_本年度每日尖峰備轉容量率(https://data.gov.tw/dataset/25850)

For this project, we'll be only using the 備轉容量(Operating Reserve) in MW for the time series prediction


## Data Analysis
This is an example of the dataset is used for training
 ![Dataset example](/images/dataset_example.png)

**Seasonal Decompose**:  
 ![Seasonal Decompose](/images/seasonal_decompose.png)
 
**Autocorrelation (ACF)**:  
 ![acf](/images/acf.png)
 Autocorrelation is the correlation of a single time series with a lagged copy of itself
**Partial Autocorrelation (PACF)**:  
 ![pacf](/images/pacf.png)
PACF can be imagined as the correlation between the series and its lag, after excluding the contributions from the intermediate lags.
Both PACF and ACF are drawn to evaluate the Auto Regressive order and Moving average order of SARIMA
## Selecting best parameters for Model fitting using auto_arima()
```
smodel = auto_arima(train, start_p=1, start_q=1,
                           test='adf',
                           max_p=7, max_q=7, m=7,
                           start_P=0, seasonal=True,
                           d=None, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True,
                           enforce_stationarity=False,
                           enforce_invertibility=False,
                           stepwise=True)
```
Returns best ARIMA model according to AIC value

**Akaike information criterion (AIC)**:  
AIC is a mathematical method for evaluating how well a model fits the data it was generated from.
- the number of independent variables used to build the model.
- the maximum likelihood estimate of the model (how well the model reproduces the data).
## Recreating the environment and run the model##
requirement libaries
```
pip3 install -r requirements.txt
```
running the code (make sure training_data.csv is in the same folder):
```
python app.py --training training_data.csv --output submission.csv
```

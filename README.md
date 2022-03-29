# DSAI_HW1

Given a time series electricity data to predict the value of the operating reserve value of each day during 2022/03/30 ~ 2022/04/13. 



## Dataset Used

Dataset is extracted from [台灣電力公司](https://data.gov.tw/).  
1.台灣電力公司_過去電力供需資訊(https://data.gov.tw/dataset/19995)  
2.台灣電力公司_本年度每日尖峰備轉容量率(https://data.gov.tw/dataset/25850)

For this project, we'll be only using the 備轉容量(Operating Reserve) in MW for the time series prediction


## Data Analysis
 ![Dataset example](/images/dataset_example.png)


**Seasonal Decompose **:  
![Seasonal Decompose](/images/seasonal_decompose.png)

## Model & Feature Selection


## Recreating the environment and run the model##
requirement libaries
```
pip3 install -r requirements.txt
```
running the code (make sure training_data.csv is in the same folder):
```
python app.py --training training_data.csv --output submission.csv
```

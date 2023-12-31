# -*- coding: utf-8 -*-
"""gold_price

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hnSUrtf3agJCvSfeJEU5pJxFMzYsc2Ym

# Gold Price Forecasting
## Author github.com/tushar2704

#Table of contents
>[Data Preparation](#scrollTo=rp26xq2apRZf)

>[Visualisations of all columns](#scrollTo=OgnR23rJpRZk)

>[Time Series Split](#scrollTo=mJ-D0r6HpRZn)

>[LGBM Regressor with Repeated stratified K fold](#scrollTo=rT7Ybbf4pRZo)

>[Above 99% accuracy in both train and test sets.](#scrollTo=0kZbg0LhpRZr)

>[Plot of actual vs Predicted](#scrollTo=mditK7TXpRZs)

![](https://images.thequint.com/thequint%2F2017-12%2Ff601a20f-6ae8-4c6a-a65b-4ddce846c017%2Fb9c83fef-a0b4-4242-9a86-6e2f4e559987.jpg?rect=0%2C0%2C724%2C407&auto=format%2Ccompress&fmt=webp)

Importing libraries and reading data from csv file
"""

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
df.head(10)

"""# Data Preparation"""

df.columns

"""Convert `Date` column to datetime type"""

df['Date'] = pd.to_datetime(df['Date'])

"""The code calculates the absolute correlation values between the 'Adj Close' column and all other columns in the DataFrame 'df', then sorts them in descending order and stores the result in 'all_corr'. Finally, it displays the 'all_corr' Series.





"""

all_corr = df.corr().abs()['Adj Close'].sort_values(ascending = False)
all_corr

"""The code creates a new Series 'corr_drop' containing only the correlation values from 'all_corr' that are less than 0.35, indicating weak correlations. It then displays the 'corr_drop' Series.





"""

corr_drop = all_corr[all_corr < 0.35]
corr_drop

"""The code creates a list 'to_drop' containing column names with weak correlations from DataFrame 'df'. It then creates a new DataFrame 'df2' by dropping the columns listed in 'to_drop' and displays the first few rows of 'df2'.






"""

to_drop = list(corr_drop.index)
df2 = df.drop(to_drop, axis = 1)
df2.head()

"""The code sets the "Date" column as the new index for DataFrame 'df2', essentially making the "Date" column the row labels. It then displays the updated 'df2' DataFrame.





"""

df2 = df2.set_index("Date")
df2

"""# Visualisations of all columns

The code imports the required modules, defines some lists and variables, and creates a function 'show_raw_visualization' to display visualizations of various features from the DataFrame 'df'. The function plots each feature's data against time using subplots and assigns different colors to each feature. The resulting visualizations are displayed using Matplotlib.
"""

import matplotlib.pyplot as plt

titles = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'SP_open', 'SP_high', 'SP_low', 'SP_close',
          'SP_Ajclose','SP_volume','DJ_open', 'DJ_high' ]
feature_keys = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'SP_open', 'SP_high', 'SP_low', 'SP_close',
                'SP_Ajclose', 'SP_volume','DJ_open', 'DJ_high']

colors = [ "blue","orange","green","red","purple","brown","pink","gray","olive", "cyan"]

date_time_key = "Date"

def show_raw_visualization(data):
    time_data = data[date_time_key]
    fig, axes = plt.subplots(
        nrows=7, ncols=2, figsize=(15, 20), dpi=80, facecolor="w", edgecolor="k"
    )
    for i in range(len(feature_keys)):
        key = feature_keys[i]
        c = colors[i % (len(colors))]
        t_data = data[key]
        t_data.index = time_data
        t_data.head()
        ax = t_data.plot(
            ax=axes[i // 2, i % 2],
            color=c,
            title="{} - {}".format(titles[i], key),
            rot=25,
        )
        ax.legend([titles[i]])
    plt.tight_layout()


show_raw_visualization(df)

"""In the given code, two lists 'titles' and 'feature_keys' are defined to specify the titles and feature names. Then, the function 'show_raw_visualization' is called with DataFrame 'df' to display visualizations of the specified features against time using Matplotlib.





"""

titles = ['DJ_low', 'DJ_close', 'DJ_Ajclose', 'DJ_volume',
       'EG_open', 'EG_high', 'EG_low', 'EG_close', 'EG_Ajclose', 'EG_volume',
       'EU_Price', 'EU_open', 'EU_high', 'EU_low']
feature_keys = ['DJ_low', 'DJ_close', 'DJ_Ajclose', 'DJ_volume',
       'EG_open', 'EG_high', 'EG_low', 'EG_close', 'EG_Ajclose', 'EG_volume',
       'EU_Price', 'EU_open', 'EU_high', 'EU_low']
show_raw_visualization(df)

"""In the given code, two lists 'titles' and 'feature_keys' are defined to specify the titles and feature names. Then, the function 'show_raw_visualization' is called with DataFrame 'df' to display visualizations of the specified features against time using Matplotlib.





"""

titles = ['EU_Trend', 'OF_Price',
       'OF_Open', 'OF_High', 'OF_Low', 'OF_Volume', 'OF_Trend', 'OS_Price',
       'OS_Open', 'OS_High', 'OS_Low', 'OS_Trend', 'SF_Price', 'SF_Open']
feature_keys = ['EU_Trend', 'OF_Price',
       'OF_Open', 'OF_High', 'OF_Low', 'OF_Volume', 'OF_Trend', 'OS_Price',
       'OS_Open', 'OS_High', 'OS_Low', 'OS_Trend', 'SF_Price', 'SF_Open']
show_raw_visualization(df)

"""In the given code, two lists 'titles' and 'feature_keys' are defined to specify the titles and feature names. Then, the function 'show_raw_visualization' is called with DataFrame 'df' to display visualizations of the specified features against time using Matplotlib.





"""

titles = ['SF_High', 'SF_Low', 'SF_Volume', 'SF_Trend', 'USB_Price', 'USB_Open',
       'USB_High', 'USB_Low', 'USB_Trend', 'PLT_Price', 'PLT_Open', 'PLT_High',
       'PLT_Low', 'PLT_Trend']
feature_keys = ['SF_High', 'SF_Low', 'SF_Volume', 'SF_Trend', 'USB_Price', 'USB_Open',
       'USB_High', 'USB_Low', 'USB_Trend', 'PLT_Price', 'PLT_Open', 'PLT_High',
       'PLT_Low', 'PLT_Trend']
show_raw_visualization(df)

"""In the given code, two lists 'titles' and 'feature_keys' are defined to specify the titles and feature names. Then, the function 'show_raw_visualization' is called with DataFrame 'df' to display visualizations of the specified features against time using Matplotlib.





"""

titles = ['RHO_PRICE', 'USDI_Price', 'USDI_Open', 'USDI_High',
       'USDI_Low', 'USDI_Volume', 'USDI_Trend', 'GDX_Open', 'GDX_High',
       'GDX_Low', 'GDX_Close', 'GDX_Adj Close', 'GDX_Volume', 'USO_Open',
       ]
feature_keys = ['RHO_PRICE', 'USDI_Price', 'USDI_Open', 'USDI_High',
       'USDI_Low', 'USDI_Volume', 'USDI_Trend', 'GDX_Open', 'GDX_High',
       'GDX_Low', 'GDX_Close', 'GDX_Adj Close', 'GDX_Volume', 'USO_Open',
       ]
show_raw_visualization(df)

"""The code defines a new function 'show_raw_visualization_small' that displays visualizations of a subset of specified features ('USO_High', 'USO_Low', 'USO_Close', 'USO_Adj Close', 'USO_Volume') against time using a smaller layout with 3 rows and 2 columns of plots. The function is then called with DataFrame 'df' to display these visualizations using Matplotlib.





"""

titles = ['USO_High', 'USO_Low', 'USO_Close', 'USO_Adj Close', 'USO_Volume']
feature_keys = ['USO_High', 'USO_Low', 'USO_Close', 'USO_Adj Close', 'USO_Volume']

def show_raw_visualization_small(data):
    time_data = data[date_time_key]
    fig, axes = plt.subplots(
        nrows=3, ncols=2, figsize=(15, 20), dpi=80, facecolor="w", edgecolor="k"
    )
    for i in range(len(feature_keys)):
        key = feature_keys[i]
        c = colors[i % (len(colors))]
        t_data = data[key]
        t_data.index = time_data
        t_data.head()
        ax = t_data.plot(
            ax=axes[i // 2, i % 2],
            color=c,
            title="{} - {}".format(titles[i], key),
            rot=25,
        )
        ax.legend([titles[i]])
    plt.tight_layout()


show_raw_visualization_small(df)

"""# Time Series Split

The code imports the TimeSeriesSplit class from scikit-learn, creates a TimeSeriesSplit object 'tss' with 6 splits for time series cross-validation. It then prepares the feature matrix 'X' by dropping the 'Adj Close' column from DataFrame 'df2', and the target vector 'y' is set to the 'Adj Close' column of 'df2'.
"""

from sklearn.model_selection import TimeSeriesSplit

tss = TimeSeriesSplit(n_splits = 6)
X = df2.drop(['Adj Close'], axis = 1)
y = df2['Adj Close']

"""The code iterates over the splits created by the TimeSeriesSplit 'tss' and extracts the corresponding training and testing sets from the feature matrix 'X' and target vector 'y'. It stores the training and testing sets in 'X_train', 'X_test', 'y_train', and 'y_test', respectively, for each iteration of the loop. This process allows for time series cross-validation.





"""

for train_index, test_index in tss.split(X):
    X_train, X_test = X.iloc[train_index, :], X.iloc[test_index,:]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

"""# LGBM Regressor with Repeated stratified K fold

The code imports the LightGBM regressor model and the necessary modules for cross-validation. It then creates an instance of the LightGBM regressor model as 'model' and a RepeatedKFold cross-validator as 'cv', which will perform repeated k-fold cross-validation with 5 splits and 3 repeats, using a random seed of 1.
"""

from lightgbm import LGBMRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

model = LGBMRegressor()
cv = RepeatedKFold(n_splits=5, n_repeats=3, random_state=1)

"""The code calculates the negative mean absolute error (MAE) scores for the LightGBM model using cross-validation on the training data. It then prints the average and standard deviation of these negative MAE scores.





"""

n_scores = cross_val_score(model, X_train, y_train, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1, error_score='raise')

from numpy import mean
from numpy import std
print('Negative MAE: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

"""The code fits the LightGBM model to the training data, then uses the model to predict the target values for the test data. It then calculates and prints the Mean Absolute Error (MAE) between the true target values ('y_test') and the predicted target values ('y_pred').





"""

model.fit(X_train, y_train)
y_pred= model.predict(X_test)
from sklearn.metrics import mean_absolute_error
print("The Mean Absolute error is: ", mean_absolute_error(y_test, y_pred))

"""The code calculates and returns the coefficient of determination (R-squared) for the LightGBM model's predictions on the test data ('X_test') and the corresponding true target values ('y_test').





"""

model.score(X_test, y_test)

model.score(X_train, y_train)

"""# Above 99% accuracy in both train and test sets.

The code creates a DataFrame named 'result' with two columns, 'Actual' and 'Predicted', containing the true target values ('y_test') and the corresponding predicted target values ('y_pred') obtained from the LightGBM model's predictions on the test data. It then displays the 'result' DataFrame.
"""

result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
result

"""# Plot of actual vs Predicted

The code selects the first 30 rows of the 'result' DataFrame and creates a bar plot to compare the actual and predicted values side by side. It adds major and minor gridlines to the plot and displays it using Matplotlib.
"""

result_plot = result.head(30)
result_plot.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
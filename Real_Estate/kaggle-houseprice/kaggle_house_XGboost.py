"""
- https://www.kaggle.com/dansbecker/learning-to-use-xgboost
- https://brunch.co.kr/@snobberys/137
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import Imputer

df = pd.read_csv('./kaggle-houseprice/train.csv')

# handling with NaNs
df = df.dropna(axis=0, subset=['SalePrice'])
col_nan=(df.isnull().sum()/len(df)).sort_values(ascending=False)[:7].index
df = df.drop(col_nan, axis=1)
df = df.fillna(df.mean())

X = df.select_dtypes(include=[np.number]).drop(['SalePrice'],axis=1).fillna(df.mean())
y = df['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X.as_matrix(), y.as_matrix(), test_size=0.25)

# my_imputer = Imputer()
# train_X = my_imputer.fit_transform(train_X)
# test_X = my_imputer.transform(test_X)

from xgboost import XGBRegressor
model_XGboost = XGBRegressor().fit(X_train, y_train, verbose=False)

"""Evaluation"""
""" (1) Mean Squared Error """
from sklearn.metrics import mean_squared_error
y_predict = model_XGboost.predict(X_test)
print ("- MSE: ", mean_squared_error(y_test,y_predict))

""" (2) r^2"""
from sklearn.metrics import r2_score
print("- r^2:", r2_score(y_test,y_predict))


"""Feature Importance"""
f_importance = model_XGboost.booster().get_score(importance_type='weight')



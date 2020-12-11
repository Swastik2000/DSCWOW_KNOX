
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib
from sklearn.preprocessing import RobustScaler
import csv
import datetime
from sklearn.svm import SVR
import sklearn.svm as svm
from sklearn.linear_model import LinearRegression




def train_data():
    x = data1.drop('Kvalitet', axis = 1)
    x = x.drop('Unnamed: 5', axis = 1)
    x = x.drop('Fran Datum Tid (UTC)', axis = 1)
    x = x.drop('Tidsutsnitt:', axis = 1)
    y = x.temperature
    X = x.drop('temperature', axis= 1)

    x2 = data2.drop('Kvalitet', axis = 1)
    x2 = x2.drop('Unnamed: 5', axis = 1)
    # x2 = x2.drop('Till Datum Tid (UTC)', axis = 1)
    x2 = x2.drop('Fran Datum Tid (UTC)', axis = 1)
    x2 = x2.drop('Tidsutsnitt:', axis = 1)
    y2 = x2.temperature
    X2 = x2.drop('temperature', axis= 1)

    new_dates = []
    counter = 0
    X = X.append(X2)
    dates = X.day
    for day in dates:
        day = datetime.datetime.strptime(day, "%Y-%m-%d")
        day2 = (day - datetime.datetime(1970,1,1)).total_seconds()
        new_dates.append(day2)
    X.day = new_dates
    new_dates= []
    for day in X.till:
        day = datetime.datetime.strptime(day, "%Y-%m-%d %H:%M:%S")
        day2 = (day - datetime.datetime(1970,1,1)).total_seconds()
        new_dates.append(day2)
    X.till = new_dates
    y = y.append(y2)


    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.5, 
                                                        random_state=123, 
                                                        )


    
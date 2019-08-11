from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_data():
    
    return pd.read_csv("data/sonar.all-data")

def get_data_description(data):
    print("Shape of the dataset: ", data.shape )
    print("Number of unique values in each column: ",data.nunique())
    print("Shape of the dataset: ", data.shape )
    
    pd.options.display.max_columns=100
    pd.options.display.float_format = '{:.4f}'.format
    
    print("little description: ", data.describe())
    print("the labels are: ", data.iloc[:,-1].unique())

def display_data_correlations(data):
    fig1, ax1 = plt.subplots()
    ax1.pcolor(data.corr(),cmap='coolwarm')
    
    fig2, ax2 = plt.subplots()
    data.corr().iloc[:,-1].plot(use_index=False, xticks=np.arange(10,70,10))

def prepare_labels(data):
    data.iloc[: , -1] = data.iloc[: , -1].replace(to_replace = 'R', value = 0)
    data.iloc[: , -1] = data.iloc[: , -1].replace(to_replace = 'M', value = 1)
    
    print("prepared labels: ", data.iloc[: , -1])

def get_numpy_data(data, nb_lines, nb_columns):
   return data.values.reshape(nb_lines, nb_columns) 

def analyze_regression_model_perfs(model, X_train, X_test, y_train, y_test, log_msg):
    model.fit(X_train, y_train)
    y_prediction_train = model.predict(X_train)
    y_prediction_test = model.predict(X_test)
    msq_train_error = mean_squared_error(y_prediction_train,y_train)
    msq_test_error = mean_squared_error(y_prediction_test,y_test)
    print("for ", log_msg, ":")
    print("msq train error: ", msq_train_error, ", msq test error: ", msq_test_error)
    print('Test R-Square:',r2_score(y_test,y_prediction_test))
    if type(model) is LogisticRegression:
        print ('Train accuracy: ', accuracy_score(y_train, y_prediction_train))
        print ('Test accuracy: ', accuracy_score(y_test, y_prediction_test))
    
if __name__ == "__main__":

    data = get_data()
    get_data_description(data)
    display_data_correlations(data)
    prepare_labels(data)
    np_data = get_numpy_data(data, 207, 61)
    
    X_train, X_test, y_train, y_test = train_test_split(np_data[:, 0:-2], np_data[:, -1], test_size=0.7)
    print("X_train = ", X_train)
    print("Y_train = ", y_train)
    
    linear_regression_model = linear_model.LinearRegression()
    analyze_regression_model_perfs(linear_regression_model, X_train, X_test, y_train, y_test, "linear regression")
    
    logistic_regression_model = LogisticRegression(solver = 'lbfgs')
    analyze_regression_model_perfs(logistic_regression_model, X_train, X_test, y_train, y_test, "logistic regression")
    
    
  
    
    
    
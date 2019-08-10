from pandas import DataFrame
from sklearn.model_selection import train_test_split

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
    
if __name__ == "__main__":

    data = get_data()
    get_data_description(data)
    display_data_correlations(data)
    prepare_labels(data)
    
    np_data = get_numpy_data(data, 207, 61)
    X_train, X_test, y_train, y_test = train_test_split(np_data[:, 0:-2], np_data[:, -1], test_size=0.7)
    print("X_train = ", X_train)
    print("Y_train = ", y_train)
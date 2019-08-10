import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/sonar.all-data") #Your code here

print("Shape of the dataset: ",df.shape )
print("Number of unique values in each column: ",df.nunique())
print("Shape of the dataset: ",df.shape )

pd.options.display.max_columns=100
pd.options.display.float_format = '{:.4f}'.format
print("little description: ", df.describe())
print("the labels are: ", df.iloc[:,-1].unique())
fig1, ax1 = plt.subplots()
ax1.pcolor(df.corr(),cmap='coolwarm')

fig2, ax2 = plt.subplots()

df.corr().iloc[:,-1].plot(use_index=False, xticks=np.arange(10,70,10))



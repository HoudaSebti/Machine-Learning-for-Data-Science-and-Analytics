import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('sonar.all-data') #Your code here
print("Shape of the dataset: ",df.shape )
print("Number of unique values in each column: ",df.nunique())
print("Shape of the dataset: ",df.shape )

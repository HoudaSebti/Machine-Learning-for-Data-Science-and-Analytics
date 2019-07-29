import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import ssl

url="https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
df = pd.read_csv(url) #Your code here
print("Shape of the dataset: ",df.shape )
print("Number of unique values in each column: ",df.nunique())
print("Shape of the dataset: ",df.shape )

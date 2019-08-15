from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_data():
    
    return pd.read_csv("data/iris.data", names=['sepal length','sepal width','petal length','petal width','target'])

def plot_data(data):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    colors = ['r', 'g', 'b']
    for target, color in zip(targets,colors):
        indicesToKeep = data['target'] == target
        ax.scatter(data.loc[indicesToKeep, 'principal component 1']
                   , data.loc[indicesToKeep, 'principal component 2']
                   , c = color
                   , s = 50)
    ax.legend(targets)
    ax.grid()

def pca_for_data_visualization(data):
    features = ['sepal length','sepal width','petal length','petal width']
    x = data.loc[:, features].values
    y = data.loc[:, ['target']].values
    x = StandardScaler().fit_transform(x)
    pca = PCA(n_components = 2)
    principal_components = pca.fit_transform(x)
    principal_data = pd.DataFrame(data = principal_components, columns = ['principal component 1', 'principal component 2'])
    print('principal data:', principal_data)
    final_data = pd.concat([principal_data, data[['target']]], axis = 1)
    plot_data(final_data)
    print('variances: ', pca.explained_variance_ratio_)
    
if __name__ == "__main__":
    data = get_data()
    print('data', data)
    pca_for_data_visualization(data)
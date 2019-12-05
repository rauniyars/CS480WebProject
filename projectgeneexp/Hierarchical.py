import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

#Importing the data set from csv file
dataset = pd.read_csv('myGeneExpData.csv')

#Extracting the attributes to be worked on in terms of variables
X = dataset.iloc[:,[2,3,4,5,6,7,8,9,10,11]].values

#Using the dendogram and determining the number of Clusters
import scipy.cluster.hierarchy as sch
dendogram=sch.dendrogram(sch.linkage(X,method='ward'))
plot.title('Dendogram')
plot.xlabel('Samples')
plot.ylabel('Eucledian Distance')
plot.show()

#Create the Model
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=3,affinity="eucledian",linkage='ward')
y_hc=hc.fit_predict(X)

plot.scatter(X[y_hc == 0,0], X[y == 0,1], s=100, c='red', label='Cluster 1')
plot.scatter(X[y_hc == 1,0], X[y == 1,1], s=100, c='blue', label='Cluster 2')
plot.scatter(X[y_hc == 2,0], X[y == 2,1], s=100, c='green', label='Cluster 3')
plot.title('Clusters')
plot.xlabel('Genes')
plot.ylabel('Samples')
plot.legend()
plot.show()

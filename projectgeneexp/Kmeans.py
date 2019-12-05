import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
from sklearn.cluster import KMeans

#Importing the data set from csv file
dataset = pd.read_csv('myGeneExpData.csv')

#Extracting the attributes to be worked on in terms of variables
X = dataset.iloc[:,[2,3,4,5,6,7,8,9,10,11]].values

#Finding the optimal number of clusters
wcss = []

for i in range(1,16): #for loop for 15 clusters
    kmeans = KMeans(n_clusters = i, init='k-means++', random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#Plotting the clusters
plot.plot(range(1,16),wcss)
plot.title('Elbow Method')
plot.xlabel('Number Of Clusters')
plot.ylabel('WCSS')
plot.show()

#K-Means Clustering
#kmeans = KMeans(n_clusters = 2, init='k-means++', random_state = 0)
#y = kmeans.fit_predict(X)

#plot.scatter(X[y == 0,0], X[y == 0,1], s=25, c='red', label='Cluster 1')
#plot.scatter(X[y == 1,0], X[y == 1,1], s=25, c='blue', label='Cluster 2')
#plot.scatter(X[y == 2,0], X[y == 2,1], s=25, c='green', label='Cluster 3')

#plot.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=25, c='yellow', label='Centroid')
#plot.title('KMeans Clustering')
#plot.xlabel('First')
#plot.ylabel('Second')
#plot.show()

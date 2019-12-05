import pandas as pd
import numpy as np

#reads the csv file titled mycsv
random = pd.read_csv('mycsv1.csv')

#returns a data frame holding the first n rows in random
data = random.head()
print(random.head())

#print(data.size)
#
#print(random[0])
dataSize = data.size
print(dataSize)
for index in range(data.size):
    for j in range(data.size - 1):
        if random[index] <= random[j+1]:
            print("Row {} is less than row {}".format(index, j+1))
        elif random[random[index] <= random[j+1]]:
            print("Row {} is greater than row {}".format(index, j+1))
        else:
            print("No relationship")

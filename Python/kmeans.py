import numpy as np
import csv
from sklearn.cluster import KMeans
import shutil as su

def kmeans(path_and_name):
    original = np.genfromtxt(path_and_name, delimiter=',')
    headless = original[1:]
    data = headless[:, 0]
    data = data.reshape(-1,1)
    print(data)
    ks = KMeans(n_clusters=3).fit(data)

    print("Labels for kmeans: ")
    labels = ks.labels_
    #labels = np.append("cluster", labels)
    print(labels)

    newdata = np.append(np.reshape(headless[:,3], (-1,1)), np.reshape(headless[:,4], (-1,1)), axis=1)
    newdata = np.append(newdata, np.reshape(headless[:,5], (-1,1)), axis=1)
    newdata = np.append(newdata, np.reshape(labels,(-1,1)), axis=1)

    np.savetxt("testdata/new.csv", newdata, delimiter=',')


kmeans("testdata/complete.csv")
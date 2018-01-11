import numpy as np
import csv
from sklearn.cluster import KMeans
import shutil as su

def kmeans(path_and_name):
    data = np.genfromtxt(path_and_name, delimiter=',')
    data = data[1:]
    data = data[:, 0]
    data = data.reshape(-1,1)
    print(data)
    ks = KMeans(n_clusters=3).fit(data)

    print("Labels for kmeans: ")
    labels = ks.labels_
    labels = np.append("cluster", labels)
    print(labels)


    #su.copyfile(path_and_name, "testdata/completenew.csv")

    with open(path_and_name, "r") as original:
        with open("testdata/complete.csv", "w") as new:
            writer = csv.writer(new)

            for row, label in zip(original, labels):
                row = np.append(row, label)

                writer.writerow(row)

kmeans("testdata/complete.csv")
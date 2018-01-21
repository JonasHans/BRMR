import numpy as np
import csv
from sklearn.cluster import KMeans
import shutil as su

def kmeans(path_and_name):
    original = np.genfromtxt(path_and_name, delimiter=',')
    headless = original[1:]

    DBZ_weight = 100
    clusters = 3
    dataDBZ = headless[:, 0]*DBZ_weight
    dataZ = headless[:, 5]

    #data = np.matrix(zip(dataDBZ, dataZ))


    # Output csv in form: DBZH, VRAD, X, Y, Z, Label
    data = np.append(np.reshape(headless[:,0], (-1,1)), np.reshape(headless[:,2], (-1,1)), axis=1)

    ks = KMeans(n_clusters=clusters).fit(data)
    labels = ks.labels_

    data = np.append(data, np.reshape(headless[:,3], (-1,1)), axis=1)
    data = np.append(data, np.reshape(headless[:,4], (-1,1)), axis=1)
    data = np.append(data, np.reshape(headless[:,5], (-1,1)), axis=1)

    labeleddata = np.append(data, np.reshape(labels,(-1,1)), axis=1)

    #filename = "DBZ="+str(DBZ_weight)+" and clusters="+str(clusters)
    #np.savetxt("output/"+filename+".csv", newdata, delimiter=',')
    np.savetxt("testdata/new.csv", labeleddata, delimiter=',')
    #print "Created csv file: "+filename

kmeans("testdata/complete.csv")

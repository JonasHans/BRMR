import numpy as np
import csv
from sklearn.cluster import KMeans
import shutil as su

def kmeans(path_and_name):
    original = np.genfromtxt(path_and_name, delimiter=',')
    headless = original[1:]


    # Output csv in form: DBZH, VRAD, X, Y, Z, Label
    data = np.append(np.reshape(headless[:,0], (-1,1)), np.reshape(headless[:,2], (-1,1)), axis=1)

    ks = KMeans(n_clusters=10).fit(data)
    labels = ks.labels_

    data = np.append(data, np.reshape(headless[:,3], (-1,1)), axis=1)
    data = np.append(data, np.reshape(headless[:,4], (-1,1)), axis=1)
    data = np.append(data, np.reshape(headless[:,5], (-1,1)), axis=1)

    labeleddata = np.append(data, np.reshape(labels,(-1,1)), axis=1)

    #filename = "DBZ="+str(DBZ_weight)+" and clusters="+str(clusters)
    #np.savetxt("output/"+filename+".csv", newdata, delimiter=',')
    np.savetxt("output/kmeans.csv", labeleddata, delimiter=',')
    #print "Created csv file: "+filename

kmeans('csvdata/160930/160930-23-00.csv')

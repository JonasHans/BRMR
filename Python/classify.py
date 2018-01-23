import numpy as np
import csv
from sklearn.cluster import KMeans
import shutil as su

def classify_rain(path_and_name):
    original = np.genfromtxt(path_and_name, delimiter=',')
    data = original[1:]
    counter=0
    classification = np.array([])

    for i in data[:,0]:
    	if(i > 7.0):
    		classification = np.append(classification, 0)
    	else:
    		counter = counter + 1
    		classification = np.append(classification, 1)
    		print(counter)

    classification = np.reshape(classification, (-1,1))



    output = np.append(np.reshape(data[:,3], (-1,1)), np.reshape(data[:,4], (-1,1)), axis=1)
    output = np.append(output, np.reshape(data[:,5], (-1,1)), axis=1)
    output = np.append(output, np.reshape(data[:,0], (-1,1)), axis=1)
    labeled_output = np.append(output, classification, axis=1)

    # output shape: X, Y, Z, DBZH, Label

    np.savetxt("testdata/classified.csv", labeled_output, delimiter=',')

classify_rain("testdata/complete.csv")
# https://github.com/clucas111/delineating-linear-elements/blob/master/Code/lin_delineation.py
# The algorithm found above is focused on finding rectangular objects instead of other shapes (like clouds) which is
# problematic for our use. It also downsamples the points to only and x and y removing the z (which is exactly what we
# didn't want)
#

import sys
import numpy as np
import matplotlib.pyplot as plt

from skimage.morphology import watershed
from skimage.segmentation import random_walker
from skimage.exposure import rescale_intensity
import skimage

def importDataFromCSV(fileName):
    original = np.genfromtxt(fileName, delimiter=',')
    data = original[1:]
    return data

def createWatershedSegmentation(data):
    # X,Y,X,DBZ
    data[:,0] = data[:,0]*10
    inputData = data[:,[3,4,5,0]]

    # Creating markers
    markers = np.zeros(inputData.shape, dtype=np.uint)

    markers[data[:,0] < 0] = 1
    markers[data[:,0] > 7] = 2

    # Generating cluster-labels with random walker segmentation algorithm
    labels = np.array(watershed(inputData, markers))

    result = np.append(inputData, np.reshape(labels[:,0],(-1,1)),axis = 1)
    np.savetxt("output/Watershed-1.csv",result, delimiter=',')

# Random walker segmentation
def createRWSegmentation(data):
    # X,Y,X,DBZ
    data[:,0] = data[:,0]*10
    inputData = data[:,[3,4,5,0]]

    # Creating markers
    markers = np.zeros(inputData.shape, dtype=np.uint)

    markers[data[:,0] < 0] = 1
    markers[data[:,0] > 7] = 2

    # Generating cluster-labels with random walker segmentation algorithm
    labels = np.array(random_walker(inputData, markers, beta=10, mode='bf'))

    result = np.append(inputData, np.reshape(labels[:,0],(-1,1)),axis = 1)
    np.savetxt("output/RW-4.csv",result, delimiter=',')

def main(argv):
    print "******************** Begin main function *******************************"
    data = importDataFromCSV('csvData/160930/160930-20-00.csv')
    # createRWSegmentation(data)
    createWatershedSegmentation(data)
    print "********************* End main function ********************************"
    pass

if __name__ == "__main__":
    main(sys.argv)

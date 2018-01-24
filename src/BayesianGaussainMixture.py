import numpy as np
import csv
from sklearn.mixture import BayesianGaussianMixture

def bgm(path_and_name):
    original = np.genfromtxt(path_and_name, delimiter=',')
    headless = original[1:]

    #xyz = headless[:,(3:5)]
    data = headless[:,(0,2,3,4,5)]

    length = np.shape(data)[0]
    ratio = 0.4
    div = int(length * ratio)
    print div
    np.random.shuffle(data)

    trainset = data[:div]
    testset = data[div:]

    mix = BayesianGaussianMixture(n_components=3, weight_concentration_prior=0.001).fit(trainset)

    labels = mix.predict(testset)
    print labels


    labeledData = np.append(testset, np.reshape(labels, (-1,1)), axis = 1)

    counter = 0

    for i in labels:
        if i != 0:
            counter = counter + 1

    print counter

    np.savetxt("output/new.csv", labeledData, delimiter=',')

bgm('testData/930-22-45.csv')

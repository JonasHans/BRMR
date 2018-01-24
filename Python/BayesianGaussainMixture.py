import numpy as np
import csv
from sklearn.mixture import BayesianGaussianMixture

def bgm(path_and_name):
    original = np.genfromtxt(path_and_name, delimiter=',')
    headless = original[1:]

    data = headless[:,(0,2,3,4,5)]

    length = np.shape(data)[0]
    ratio = 0.4
    div = int(length * ratio)
    np.random.shuffle(data)

    trainset = data[:div]
    testset = data[div:]

    mix = BayesianGaussianMixture(n_components=6,max_iter=10000,weight_concentration_prior_type='dirichlet_distribution', weight_concentration_prior=0.00005).fit(trainset)
    print("Trainingsset fitted")

    labels = mix.predict(testset)
    print("Testset predicted")


    labeledData = np.append(testset, np.reshape(labels, (-1,1)), axis = 1)

    np.savetxt("output/new.csv", labeledData, delimiter=',')

bgm('csvdata/160930/160930-23-00.csv')

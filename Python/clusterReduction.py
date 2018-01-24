import numpy as np


def reduction(filename):
	# Generate numpy array from csv and get the last column (the labels)
	data = np.genfromtxt(filename, delimiter = ',')
	print(np.shape(data))
	lastColumn = np.shape(data)[1]-1

	# Define dictionaries
	labelDict = {}
	classDict = {}

	# Compute how many clusters there are
	clusters = np.unique(data[:,lastColumn])

	# Make a list per cluster with the DBZ values
	for i, j in zip(data[:,0],data[:,lastColumn]):
		if(str(j) in labelDict):
			labelDict[str(j)] = np.append(labelDict[str(j)], i)
		else:
			labelDict[str(j)] = np.array([i])

	# For each of the lists in labelDict, compute the average. If that average
	# is higher than 0 we classify the cluster as rain(1), else as bird(0)
	for i in labelDict:
		classDict[str(i)] = np.average(labelDict[str(i)])
		print(classDict[str(i)])
		if(classDict[str(i)] > 0):
			classDict[str(i)] = 1.0
		else:
			classDict[str(i)] = 0.0

	# Define array of the right shape, using np.empty for effifiency.
	classes = np.empty([np.shape(data)[0],1], float)
	
	#
	for i, j in zip(data[:,lastColumn], range(len(classes))):
		classes[j] = classDict[str(i)]

	classifiedData = np.append(data, classes, axis = 1)
	print(classifiedData)

	np.savetxt("output/classified.csv", classifiedData, delimiter=',')

reduction("output/new.csv")

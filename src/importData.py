import numpy as np
original = np.genfromtxt('csvData/160930/160930-00-00.csv', delimiter=',')
headless = original[1:]
dBZ = headless[:, 0]
X = headless[:, 3]
Y = headless[:, 4]
Z = headless[:, -1]
min_max_scaler = preprocessing.MinMaxScaler()
dbZ_normalized = min_max_scaler.fit_transform(dBZ.reshape(-1,1))
X_normalized = min_max_scaler.fit_transform(X.reshape(-1,1))
Y_normalized = min_max_scaler.fit_transform(Y.reshape(-1,1))
Z_normalized = min_max_scaler.fit_transform(Z.reshape(-1,1))
data = dbZ_normalized
data = np.zeros((len(dbZ_normalized), 4))
data[:,0] = dbZ_normalized[:,0]
data[:,1] = X_normalized[:,0]
data[:,2] = Y_normalized[:,0]
data[:,3] = Z_normalized[:,0]

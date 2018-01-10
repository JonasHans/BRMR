import numpy as np
import csv
from sklearn.cluster import MeanShift

data = np.genfromtxt('/Users/jeroenvanbaarle/Documents/Studie/Leren_en_Beslissen/skipzero1.csv', delimiter=',')
data = data[1:]
ms = MeanShift().fit(data)


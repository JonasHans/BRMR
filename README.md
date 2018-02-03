# BRMR
Bird Recognition from Meteorological Radars 
## Introduction
For this project we received raw radar data (h5 files) and the desired output is a clustered pointcloud based on the clusters rain and birds.
Here we tried various cluster techniques and described which has the best result for radarclustering.
## Contents
* `utils` (convert h5 to csv files)
	+ Make 2 folders in your utils map one empty named "csvData", another named "RadarData" containing the h5 files,
	+ Run everything in the Utilities.ipynb (This may take a while depending on how much files you have.)
	+ Copy the csvData folder to the src folder
* `src` (for the Python 2 notebooks containing the algorithms)
	+ All the algorithms are run from their separate notebooks.
	+ If an algorithm returns more than 2 clusters, run clusterReduction.ipynb to reduce that down to 2.
	+ Output files of the clusterReduction.ipynb will have the "class_" prefix to their name.
## Software used:
* CloudCompare (visualization of pointclouds)
* Python 2 + 3 (notebooks are in Python 2)
* Scikit packages (sklearn)
* numpy
* h5py (h5 file handling)
* Various other imports



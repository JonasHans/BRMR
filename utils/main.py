from fileWriter import *
from binstoxyz import *
import os
import fnmatch
import sys

# This file is for turning the h5 data to a compatible csv file.
# In fileWriter the data (in dictionaries) is written in a csv
# In binstoxyz the data from h5 is handled to calculate the coordinates and putting the data in a dictionary

# Change the code below to the folder/path of the h5 files (location)
# Target_location is where the csv data are written to
location = 'RadarData'
target_location = 'csvData'

operating_system = sys.platform

def convertH5toCSV(h5file, csvfileName):
    # Get data from h5 file
    datasets = h5py.File(h5file, 'r')

    # Convert h5 file to xyz
    points = add_heights(datasets) # From binstoxyz

    # Export points to csv file
    createCSVfile(csvfileName, points) # From fileWriter

def importData(location, newpath):
    matches = []
    # Get all h5 radar files in the radarData directory
    for root, dirnames, filenames in os.walk(location):
        for filename in fnmatch.filter(filenames, '*.h5'):
            matches.append(os.path.join(root, filename))
    if operating_system == 'windows':
        # Convert all H5 files to csv files
        for h5file in matches:
            split = h5file.split('\\') # [day, hour, quarter of an hour]
            if not os.path.exists(newpath+split[1]):
                os.makedirs(newpath+split[1])
            csvFileName = newpath+"\\"+split[1]+"\\"+split[1]+"-"+split[2]+"-"+split[3]+".csv"
            convertH5toCSV(h5file, csvFileName)
    else:
        # Convert all H5 files to csv files
        for h5file in matches:
            split = h5file.split('/') # [day, hour, quarter of an hour]
            regexResult = split
            if not os.path.exists(newpath+"/"+split[1]):
                os.makedirs(newpath+"/"+split[1])
            csvFileName = newpath+"/"+split[1]+"/"+split[1]+"-"+split[2]+"-"+split[3]+".csv"
            convertH5toCSV(h5file, csvFileName)


def main(argv):
    print "******************** Creating CSV files *******************************"
    importData(location, target_location);
    print "********************* CSV files created ********************************"
    pass

if __name__ == "__main__":
    main(sys.argv)

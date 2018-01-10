from fileWriter import *
from binstoxyz import *
import fnmatch
import os
import re

def convertH5toCSV(h5file, csvfileName):
    # Get data from h5 file
    datasets = h5py.File(h5file,'r')
    
    # Convert h5 file to xyz
    points = add_heights(datasets)

    # Export points to csv file
    createCSVfile(csvfileName, points)

def importData():
    matches = []

    # Get all h5 radar files in the radarData directory
    for root, dirnames, filenames in os.walk('RadarData'):
        for filename in fnmatch.filter(filenames, '*.h5'):
            matches.append(os.path.join(root, filename))

    # Convert all H5 files to csv files
    for h5file in matches:
        regexResult = h5file.split('\\') # [datum, uur, kwartier]

        if not os.path.exists("csvData/"+regexResult[1]):
            os.makedirs("csvData/"+regexResult[1])

        csvFileName = "csvData/"+regexResult[1]+"/"+regexResult[1]+"-"+regexResult[2]+"-"+regexResult[3]+".csv"
        convertH5toCSV(h5file, csvFileName)


def main(argv):
    print "******************** Begin main function *******************************"
    importData();
    print "********************* End main function ********************************"
    pass

if __name__ == "__main__":
    main(sys.argv)
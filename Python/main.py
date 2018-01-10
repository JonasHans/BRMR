from fileWriter import *
from binstoxyz import *

def convertH5toCSV(h5file, csvfileName):
    # Get data from h5 file
    datasets = h5py.File(h5file,'r')

    # Convert h5 file to xyz
    points = add_heights(datasets)

    # Export points to csv file
    createCSVfile(csvfileName, points)

def main(argv):
    print "******************** Begin main function *******************************"
    convertH5toCSV("testData/nldbl_pvol_20160930T0000Z.h5","output/test3.csv" )
    print "********************* End main function ********************************"
    pass

if __name__ == "__main__":
    main(sys.argv)

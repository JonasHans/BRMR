from fileWriter import *
from binstoxyz import *

def testDataSet():
    datasets = h5py.File('testData/nldbl_pvol_20160930T0000Z.h5','r')
    points = add_heights(datasets)
    createCSVfile("firstDataSet", points)

def main(argv):
    print "******************** Begin main function *******************************"
    testDataSet();
    # testFileWriters()
    print "********************* End main function ********************************"
    pass

if __name__ == "__main__":
    main(sys.argv)

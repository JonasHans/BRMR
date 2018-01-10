import csv
import laspy
import sys
import numpy as np
import time

# ["X","Y","Z","Intensity"]
def createCSVfile(fileName, data):
    print "Creating CSV file: ",fileName

    with open(fileName, 'w') as csvfile:
        fieldnames = ['x', 'y', 'z', 'DBZH']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for point in data:
            writer.writerow(point)

def createLASfile(fileName, data):
    print "Creating LAS file: ", fileName

    # Create las file header
    header = laspy.header.Header()

    # Create outpute file with header
    lasFile = laspy.file.File("output/"+fileName+".las", mode="w", header=header)
    lasFile.X = data[0]
    lasFile.Y = data[1]
    lasFile.Z = data[2]
    lasFile.intensity = data[3]
    lasFile.close()

def testFileWriters():
    data = [
    [0,0,1,1,0,0,1,1],
    [0,1,0,1,0,1,0,1],
    [0,0,0,0,1,1,1,1],
    [100, 10, 25, 60, 150, 200, 124, 144]
    ]
    createCSVfile("cube", np.transpose(data))

def main(argv):
    testFileWriters()
    pass

if __name__ == "__main__":
    main(sys.argv)

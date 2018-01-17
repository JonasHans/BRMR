import csv
import laspy
import sys
import numpy as np
import time

# ["X","Y","Z","Intensity"]
def createCSVfile(fileName, data):
    print "Creating CSV file: ",fileName

    with open(fileName, 'w') as csvfile:
        fieldnames = ['DBZH', 'TH', 'VRAD','x', 'y', 'z']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for point in data:
            if point['DBZH'] != 0.0:
                writer.writerow(point)
        csvfile.close()

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

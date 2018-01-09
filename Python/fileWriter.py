import csv
import laspy

def createCSVfile(fileName, data):
    print("Creating CSV file: ",fileName)
    with open(fileName+".csv", 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def createLASfile(fileName, data):
    print("Creating LAS file: ", fileName)

    # Create las file header
    header = laspy.header.Header()

    # Create outpute file with header
    lasFile = laspy.file.File(fileName+".las", mode="w", header=header)
    lasFile.X = data["X"]
    lasFile.Y = data["Y"]
    lasFile.Z = data["Z"]
    lasFile.intensity = data["intensity"]
    lasFile.close()

createCSVfile("test1", ["write","test"])
data = {
'X' : [1,2,3],
'Y' : [0,0,0],
'Z' : [10,10,11],
'intensity' : [25, 100, 200]
}
createLASfile("LasTEst", data)

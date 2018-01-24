import csv

# We have used the same threshold as the KNMI where everything below a dBZH value of -30 is clutter
threshold = -31.0
# Create or overwrite a csv file with 6 colomns, each containing a feature or coordinate.
def createCSVfile(fileName, data):
    print fileName

    with open(fileName, 'w') as csvfile:
		# These are the features stored each in a different colomn
        fieldnames = ['DBZH', 'TH', 'VRAD','x', 'y', 'z']
        # Write the features to a dictionary
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write a row with the specified fieldnames
        writer.writeheader()

        # Recursively write a row
        for point in data:
            if point['DBZH'] > threshold:
                writer.writerow(point)
        print 'is created.'
        csvfile.close()

<<<<<<< HEAD
import h5py
import numpy as np
import math

""" add_heights voegt de data van radarbeelden van verschillende hoogten samen tot een lijst met dictonaries
    met DBHZ waarden en coordinaten."""
def add_heights(datasets):
    points = []
    for data in datasets:
        if (data != "how" and data != "what" and data != "where"):
            elevation_angle = datasets[data]["where"].attrs.values()[1]
            nbins = datasets[data]["where"].attrs.values()[2]
            nrays = datasets[data]["where"].attrs.values()[3]
            bin_distance = datasets[data]["where"].attrs.values()[4]
            dat = datasets[data]["data1"]["data"][()]
            points.extend(get_coordinates_picture(nbins, nrays, elevation_angle, bin_distance, dat))

    return points

""" get_coordinates_picture berekent van elk punt in een radarafbeelding zijn x,y en z coordinaat
    deze worden opgeslagen in een lijst van dictionaries samen met de DBZH waarde van elk punt."""
def get_coordinates_picture(nbins, nrays, elevation_angle, bin_distance, data):
    resultset = []

    pic = []
    for bin_number in range(nbins):
        for ray_number in range(nrays):
            tmp = {"DBZH": data[ray_number][bin_number], "coordinates": get_xyz(elevation_angle, bin_number, bin_distance, ray_number, nrays)}
            # print tmp
            pic.append(tmp)
            # resultset.append(get_xyz(elevation_angle, bin_number, bin_distance, ray_number, nrays).append(data[ray_number][bin_number])) # [x,y,z,i]
    return pic


"""# get_xyz berekent de x, y en z coordinaat van een radarbin.
    INPUT:
    elevation angle: de hoek van de radarbeam t.o.v. de grond
    bin_number: de n-de radarbin van een beam
    bin_distance: de afstand tussen de radarbins
    angle_number: de n-de beam van de radar in de x-y richting
    total_angles: het totaal aantal beams wat is genomen in een rondje
    OUTPUT:
    de x, y, en z coordinaat van de radabin"""
def get_xyz(elevation_angle, bin_number, bin_distance, angle_number, total_angles):
    z = bin_number * bin_distance * math.sin(math.radians(elevation_angle))
    dis = bin_number * bin_distance * math.cos(math.radians(elevation_angle))
    beam_angle = (math.radians(float(angle_number)/total_angles) * 360)
    y = dis * math.cos(beam_angle)
    x = dis * math.sin(beam_angle)
    return [x,y,z]
=======
import h5py
import numpy as np
import math
import csv


datasets = h5py.File(r'C:\Users\Emmaa\Downloads\160930\30\00\00\merged\nldbl_pvol_20160930T0000Z.h5','r')

""" add_heights voegt de data van radarbeelden van verschillende hoogten samen tot een lijst met dictonaries 
    met DBHZ waarden en coordinaten."""  
def add_heights(datasets):
    points = []
    for data in datasets:
        if (data != "how" and data != "what" and data != "where"):
            elevation_angle = datasets[data]["where"].attrs.values()[1]
            nbins = datasets[data]["where"].attrs.values()[2]
            nrays = datasets[data]["where"].attrs.values()[3]
            bin_distance = datasets[data]["where"].attrs.values()[4]
            dat = datasets[data]["data1"]["data"][()]
            points.extend(get_coordinates_picture(nbins, nrays, elevation_angle, bin_distance, dat))
    return points

""" get_coordinates_picture berekend van elk punt in een radarafbeelding zijn x,y en z coordinaat
    deze worden opgeslagen in een lijst van dictionaries samen met de DBZH waarde van elk punt."""    
def get_coordinates_picture(nbins, nrays, elevation_angle, bin_distance, data):
    pic = []
    for bin_number in range(nbins):
        for ray_number in range(nrays):
            xyz = get_xyz(elevation_angle, bin_number, bin_distance, ray_number, nrays)
            tmp = {"DBZH": data[ray_number][bin_number], "x": xyz[0], "y": xyz[1], "z": xyz[2]}
            #print tmp
            pic.append(tmp)
    return pic
            

"""# get_xyz berekend de x, y en z coordinaat van een radarbin.
    INPUT:
    elevation angle: de hoek van de radarbeam t.o.v. de grond
    bin_number: de n-de radarbin van een beam
    bin_distance: de afstand tussen de radarbins
    angle_number: de n-de beam van de radar in de x-y richting
    total_angles: het totaal aantal beams wat is genomen in een rondje
    OUTPUT:
    de x, y, en z coordinaat van de radabin"""    
def get_xyz(elevation_angle, bin_number, bin_distance, angle_number, total_angles):
    z = bin_number * bin_distance * math.sin(math.radians(elevation_angle))
    dis = bin_number * bin_distance * math.cos(math.radians(elevation_angle))
    beam_angle = (math.radians(float(angle_number)/total_angles) * 360)
    y = dis * math.cos(beam_angle)
    x = dis * math.sin(beam_angle)
    return [x,y,z]
    
points = add_heights(datasets) 

with open(r'C:\Users\Emmaa\Documents\Studie\KI\skipzero.csv', 'w') as csvfile:
    fieldnames = ['DBZH', 'x', 'y', 'z']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    # skip points where DBHZ is 0
    for point in points:
        if point["DBZH"] != 0.0:
            writer.writerow(point)


    

>>>>>>> f0ab00be7f4c3ec510d96b5d7aa299b89c1e8685

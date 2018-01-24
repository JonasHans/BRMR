import h5py
import math

# add_heights voegt de data van radarbeelden van verschillende hoogten samen tot een lijst met dictonaries
# met DBHZ waarden en coordinaten.

def add_heights(datasets):
    points = []
    for data in datasets:
        if (data != "how" and data != "what" and data != "where"):
            elevation_angle = datasets[data]["where"].attrs.values()[1]
            nbins = datasets[data]["where"].attrs.values()[2]
            nrays = datasets[data]["where"].attrs.values()[3]
            bin_distance = datasets[data]["where"].attrs.values()[4]
            data_DBZH = datasets[data]["data1"]["data"][()]
            data_TH = datasets[data]["data2"]["data"][()]
            data_VRAD = datasets[data]["data3"]["data"][()]
            offsets = [datasets[data]["data1"]["what"].attrs.values()[1], datasets[data]["data2"]["what"].attrs.values()[1], datasets[data]["data3"]["what"].attrs.values()[1]]
            gains = [datasets[data]["data1"]["what"].attrs.values()[0], datasets[data]["data2"]["what"].attrs.values()[0], datasets[data]["data3"]["what"].attrs.values()[0]]
            points.extend(get_coordinates_picture(nbins, nrays, elevation_angle, bin_distance, data_DBZH, data_TH, data_VRAD, offsets, gains))
    return points

# get_coordinates_picture berekent van elk punt in een radarafbeelding de bijbehorende x,y en z coordinaat
# deze worden opgeslagen in een lijst van dictionaries samen met de DBZH waarde van elk punt.
def get_coordinates_picture(nbins, nrays, elevation_angle, bin_distance, data_DBZH, data_TH, data_VRAD, offsets, gains):
    pic = []
    for bin_number in range(nbins):
        for ray_number in range(nrays):
            xyz = get_xyz(elevation_angle, bin_number, bin_distance, ray_number, nrays)
            tmp = {"DBZH": offsets[0] + data_DBZH[ray_number][bin_number]*gains[0], "TH":offsets[1] + data_TH[ray_number][bin_number]*gains[1],
            "VRAD":offsets[2] + data_VRAD[ray_number][bin_number] * gains[2], "x": xyz[0], "y": xyz[1], "z": xyz[2]}
            pic.append(tmp)
    return pic


#    get_xyz berekent de x, y en z coordinaat van een radarbin.
#    INPUT:
#    elevation angle: de hoek van de radarbeam t.o.v. de grond
#    bin_number: de n-de radarbin van een beam
#    bin_distance: de afstand tussen de radarbins
#    angle_number: de n-de beam van de radar in de x-y richting
#    total_angles: het totaal aantal beams wat is genomen in een rondje
#    OUTPUT:
#    de x, y, en z coordinaat van de radabin
def get_xyz(elevation_angle, bin_number, bin_distance, angle_number, total_angles):
    z = bin_number * bin_distance * math.sin(math.radians(elevation_angle))
    dis = bin_number * bin_distance * math.cos(math.radians(elevation_angle))
    beam_angle = (math.radians(float(angle_number)/total_angles) * 360)
    y = dis * math.cos(beam_angle)
    x = dis * math.sin(beam_angle)
    return [x,y,z]

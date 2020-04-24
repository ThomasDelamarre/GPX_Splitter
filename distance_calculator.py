from math import *

def getLat(trkpt):
    lat = ""
    for line in trkpt:
        index = line.find("lat")
        if (index > 0):
            line = line [index+5:]
            i = 0
            while line[i] != '\"':
                lat += line[i]
                i += 1
    return float(lat)

def getLon(trkpt):
    lon = ""
    for line in trkpt:
        index = line.find("lon")
        if (index > 0):
            line = line [index+5:]
            i = 0
            while line[i] != '\"':
                lon += line[i]
                i += 1
    return float(lon)

def getEle(trkpt):
    ele = ""
    for line in trkpt:
        index = line.find("ele")
        if (index > 0):
            line = line [index+4:]
            i = 0
            while line[i] != '<':
                ele += line[i]
                i += 1
    return float(ele)

def getCoords(trckp):
    return (getLat(trckp), getLon(trckp), getEle(trckp))


def getDistanceAndElevBtw2PointsInMeters(trckp_1, trckp_2):
    lat_1, lon_1, ele_1 = getCoords(trckp_1)
    lat_2, lon_2, ele_2 = getCoords(trckp_2)

    dLat = lat_2 - lat_1
    dLon = lon_2 - lon_1

    rad_lat_1 = radians(lat_1)
    rad_lat_2 = radians(lat_2)
    rad_dLat = radians(dLat)
    rad_dLon = radians(dLon)
    earth_radius = 6371000

    a = sin((rad_dLat)/2)*sin((rad_dLat)/2) + cos(rad_lat_1)*cos(rad_lat_2)*sin(rad_dLon/2)*sin(rad_dLon/2)
    b = 2 * atan2(sqrt(a), sqrt(1-a))
    dist = earth_radius*b

    elev = ele_2 - ele_1
    elevPlus = 0
    elevMoins = 0
    if elev > 0:
        elevPlus = elev
    else:
        elevMoins = elev

    return{"distance": dist, "elevPlus": elevPlus, "elevMoins": elevMoins}



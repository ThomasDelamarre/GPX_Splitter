from distance_calculator import getDistanceAndElevBtw2PointsInMeters
import os
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as tkMessageBox


def createGpxFiles(file_data):

    trackpoints = file_data["trackpoints"]

    max_dist = int(tkSimpleDialog.askstring("Lenght of a GPX (in km)", "Enter the length for each gpx (in km):"))*1000
    new_act_name = tkSimpleDialog.askstring("File name", "Enter base name for files: ( / to keep same as before)")

    if new_act_name != "/":
        file_data["name"] = new_act_name

    trackpoints_ids = getTrackpointsSplitIds(max_dist, trackpoints)

    for i in range (len(trackpoints_ids)-1):
        trackpoints_sub = trackpoints[trackpoints_ids[i]: trackpoints_ids[i+1]]
        print(file_data["name"])
        createNewGpx(file_data, trackpoints_sub, i+1, len(trackpoints_ids)-1)

    tkMessageBox.showinfo(title="Success", message="The files have been created on the Desktop")




def getTrackpointsSplitIds(max_dist, trackpoints):
    trackpoints_split_ids = [0]
    i = 0
    total_dist = 0

    while i < (len(trackpoints) - 1):
        distance = 0

        while (distance < max_dist and i < len(trackpoints) - 1):
            distance += getDistanceAndElevBtw2PointsInMeters(trackpoints[i], trackpoints[i + 1])["distance"]
            i = i + 1
        end_id = i

        total_dist += distance

        trackpoints_split_ids += [end_id]
    return(trackpoints_split_ids)


def createNewGpx(file_data, trackpoints, number, number_of_splits):

    filename = file_data["name"] + " part " + str(number) + "." + str(number_of_splits) + ".gpx"
    path = os.path.join('C:/Users/thoma/Desktop/Gpx Files', filename)
    if not os.path.exists('C:/Users/thoma/Desktop/Gpx Files'):
        os.makedirs('C:/Users/thoma/Desktop/Gpx Files')

    file = open(path, "w+", encoding="utf-8")

    for line in file_data["metadata"]:
        file.write(line + "\n")

    file.write("<trk>" + "\n")
    file.write("<name>" + file_data["name"] + " part" + str(number) + "/" + str(number_of_splits) + "</name>" + "\n")
    file.write("<type>" + file_data["type"] + "</type>" + "\n")
    file.write("<trkseg>" + "\n")

    for trackpoint in trackpoints:
        for line in trackpoint:
            file.write(line + "\n")

    file.write("</trkseg>" + "\n")
    file.write("</trk>" + "\n")
    file.write("</gpx>")



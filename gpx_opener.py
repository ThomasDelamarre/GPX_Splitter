from gpx_reader import *
import tkinter
from tkinter.filedialog import askopenfilename

def getDataFromFile():
    file = openFile()
    gpx_file_lines = __getLines(file)
    metadata = getMetadata(gpx_file_lines)
    activity_name = getName(gpx_file_lines)
    activity_type = getType(gpx_file_lines)
    trackpoints = getTrackPoints(gpx_file_lines)
    return {"metadata": metadata, "name": activity_name, "type": activity_type, "trackpoints": trackpoints}

def openFile():
    tkinter.Tk().withdraw()
    filename = askopenfilename()
    gpx_file = open(filename, 'r', encoding="utf-8")
    return(gpx_file)

def __getLines(file):
    text = file.read()
    lines = []
    i = 0
    while i < (len(text)-1):
        line = ""
        while text[i] != "\n" and i < (len(text)-1):
            line += text[i]
            i+=1
        i += 1
        lines += [line.strip()]
    return (lines)








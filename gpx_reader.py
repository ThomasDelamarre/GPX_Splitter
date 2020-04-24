def getMetadata(lines):
    metadata = []
    i = 0
    line = lines[i]
    while line.strip() != "</metadata>":
        metadata += [line]
        i += 1
        line = lines[i]

    metadata += [line]  # To include closing metadata
    return metadata


def getName(lines):
    i = 0
    line = lines[i]
    while line.strip()[:6] != "<name>":
        i += 1
        line = lines[i]

    return line[6:-7]


def getType(lines):
    i = 0
    line = lines[i]
    while line.strip()[:6] != "<type>":
        i += 1
        line = lines[i]

    return line[6:-7]


def getTrackPoints(lines):
    trackpoints = []
    i = 0
    while i < (len(lines) - 1):
        if lines[i][:6] == "<trkpt":
            trackpoint = []
            while lines[i].strip() != "</trkpt>":
                trackpoint += [lines[i]]
                i += 1
            trackpoint += [lines[i]]

            trackpoints += [trackpoint]
        i += 1

    return trackpoints

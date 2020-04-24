from gpx_opener import openFile, getDataFromFile
from gpx_creator import createGpxFiles

def main():
    file_data = getDataFromFile()
    createGpxFiles(file_data)

if __name__ == "__main__":
    main()
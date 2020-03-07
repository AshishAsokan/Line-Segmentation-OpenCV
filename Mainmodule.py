# Importing all necessary modules
import Segmentation
import os

# Defining function to determine file path
def inputFind():
    name = input("Enter the file name: ")
    lol = input("Enter file extension: ")
    stri = name+"."+lol

    # Setting variables to search for path
    path=['E:\\']; path1=[]; npath=" "
    for pathn in path:

        # Using os.walk() to walk through the directories
        for root, dirs, files in os.walk(pathn):
            for names in files:
                if names ==stri:
                    npath = os.path.join(root, names)
                    path1.append(npath)
                    break

    # Checking if file has been found
    if len(path1) == 0:
        # If file has not been found, raise exception
        raise FileNotFoundError
    else:
        return path1[0]

# Handling exception raised by inputfind()
try:
    path = inputFind()
    sample = Segmentation.LineSegment(path)
    sample.connectComponents()
    sample.Watershed()
    sample.disp_image()
except FileNotFoundError:
    print("Error! The specified file could not be found")
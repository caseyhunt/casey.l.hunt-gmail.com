# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:33:08 2020

@author(s): Casey & Aarjav
"""


import numpy as np
import cv2
import os
import shutil
import json

"""variable definitions"""
photo_array = []
directory = os.path.dirname(os.path.abspath(__file__))
#this is where your source goes
source = directory + "/images/"
#this is where your destination goes
destination = directory + "/images_2"
#this is the location of the json file
jsonFile = directory + "/puertorican/puertorican.json"

def openJSON():
    with open(jsonFile) as f:
        data = json.load(f)
        print(data)

"""
Gets all image names from specified directory
"""
def get_images_from_directory():
    for filename in os.listdir(source):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            photo_array.append(filename)
        else:
            continue
        
        
        
"""
computer vision stuff we need to flush through :)
TODO: identify only one face
"""
def compVis(pic):
    image = "images/" + pic
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    numFaces = len(faces)
    print("image name ", pic, " number of faces= ", numFaces)
    return(numFaces)

"""copy file to new directory if there is one face in the picture
Enter your source and destination in variable definitions above"""
def copyToDir(origDir):
    for picture in origDir:
        if compVis(picture) == 1:
            fileSrc = source + picture
            fileDest = destination
            shutil.copy(fileSrc, fileDest)
            print(picture, "copied successfully")
        else:
            print(picture, "not copied")
            
            
        
"""
Main function
"""
def main():
    compVis("1.jpg")
    get_images_from_directory()
    print(np.array(photo_array))
    copyToDir(photo_array)
    #openJSON()

if __name__== "__main__":
    main()

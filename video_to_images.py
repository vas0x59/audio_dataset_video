import os
import glob
import pandas as pd
import argparse
import xml.etree.ElementTree as ET
import cv2
from imutils import paths

path = "video_out"
path_out = "images_out"

videoPaths = sorted(list(paths.list_files(path)))
print(videoPaths)
# random.seed(42)
# random.shuffle(imagePaths)
def crop(image):
    h = image.shape[0] 
    w = image.shape[1] 
    image = image[0:h, 0:w//2]
    return image
videoPaths = [
    "video_out/The_Show_Must_Go_On/The_Show_Must_Go_On_150_16000_72_out_3.avi",
    "video_out/We_Are_The_Champions/We_Are_The_Champions_16000_72_out_3.avi",
    "video_out/We_Will_Rock_You/We_Will_Rock_You_150_16000_72_out_3.avi"
]
for videoPath in videoPaths:
    cap = cv2.VideoCapture(videoPath)
    print(videoPath)
    i = 0
    ret = True
    while ret:
        ret, image = cap.read()
        if ret == False:
            break
        if i % 2 == 0:
            # print(videoPath, i)
            label = videoPath.split(os.path.sep)[-2]
            name = videoPath.split(os.path.sep)[-1].split(".")[0]
            image = crop(image)
            cv2.imwrite(path_out + "/" + label  + "/" + name + str(i) + ".jpg", image)
        i+=1
    print(videoPath, "total:", i)
    cap.release()

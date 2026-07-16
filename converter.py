import os
import cv2
import numpy as np
import glob

# files = glob.glob("gf-ek9(120)/6/*")

"""
for file in files:
    print(file)
    path = str(file)
    img = cv2.imread(path)

    for n in range(95,254,1):
        img = np.where(img==[n,n,n], [255,255,255], img)

    cv2.imwrite(path, img)
"""

files = glob.glob('*.png')
for file in files:
    print(file)
    path = str(file)
    img = cv2.imread(path)

    # Change pixels with RGB values from 95 to 253 to white
    for n in range(95,254):
        img = np.where(img==[n,n,n], [255,255,255], img)

    cv2.imwrite(path, img)
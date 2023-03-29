
import cv2 
import sys 
import numpy as np 
args = sys.argv

path = args[1]
path = args[2]
name = path.upper()
path = path + '.png'


qr = cv2.imread(path)
height, width, ch = qr.shape
add = np.ones([height + 60, width,3])*255
add[0:height, 0:width] = qr 
origin = int((450 - len(name)*35)/2)
add = cv2.putText(add, name, (origin
                              ,height + 30), cv2.FONT_HERSHEY_DUPLEX, 
                   2, (0,0,0), 5, cv2.LINE_8)



add = cv2.resize(add, (int(add.shape[1] * 0.65), int(add.shape[0] * 0.65)))
add = cv2.morphologyEx(add, cv2.MORPH_DILATE, (5,5))

cv2.imwrite(path, add)
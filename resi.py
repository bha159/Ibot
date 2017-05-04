import cv2
import os

#This program all images in the folder to same size to use for training.
dirname = 'data'
for i in range(5,1405):
    if i in range(183,190):
        continue
    else:
        l = 'E'+str(i)+'L.jpg'
        r = 'E'+str(i)+'R.jpg'
        LE = cv2.imread(l)
        cv2.imwrite(os.path.join(dirname, 'E'+str(i)+'L.jpg'), cv2.resize(LE,(53,23)))
        RE = cv2.imread(r)
        cv2.imwrite(os.path.join(dirname, 'E'+str(i)+'R.jpg'), cv2.resize(LE,(53,23)))

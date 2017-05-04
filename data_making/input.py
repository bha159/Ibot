import numpy as np
import cv2

filel = open('inl1.txt', mode='a')
filer = open('inr1.txt', mode='a')

for i in range(5,1405):
    if i in range(183,190):
        continue
    else:
        # filel.write('[')
        # filer.write('[')
        l = 'E'+str(i)+'L.jpg'
        r = 'E'+str(i)+'R.jpg'
        LE = cv2.imread(l)
        LEa = LE.reshape(1,3657)
        LEb = LEa.ravel()
        LEz = ','.join([str(i) for i in LEb])
        filel.write(LEz)
        RE = cv2.imread(r)
        REa = RE.reshape(1,3657)
        REb = REa.ravel()
        REz = ','.join([str(i) for i in REb])
        filer.write(REz)
        filel.write('\n')
        filer.write('\n')

filel.close()
filer.close()

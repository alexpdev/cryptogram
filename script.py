import os
import sys
import cv2
import numpy as np

images = "images/crypto1.png"
img = cv2.imread(images)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i = 0
counter = {}
upper = -8
under = 8
left = -3
right = 80
counter, record = {}, []
for contour in contours:
    y1,x1 = contour[0][0]
    sub = threshold[x1+upper : x1+under, y1+left : y1+right]
    m = np.where(sub==0)
    l = len(set(m[0]))
    if l <= 4:
        try:
            pxls = sorted(set(m[1]))
            last = i = pxls[0]
            for j in pxls[1:]:
                if j == i + 1:
                    i = j
                else:
                    break
            counter.setdefault((l,i - last), 0)
            counter[(l,i-last)] += 1
            record.append([x1-l,x1+l,y1-2,y1+i-last+2])
            cv2.imshow("window", threshold[x1-l:x1+l,y1-2:y1+i-last+2])
            cv2.waitKey()
        except IndexError:
            continue
print(counter, record)

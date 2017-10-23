import cv2
import numpy as np

file_name = "../img/lightning.png"
img = cv2.imread(file_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY_INV)

im, contours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contr = contours[0]

(x,y), radius = cv2.minEnclosingCircle(contr)
center = (int(x), int(y))
radius = int(radius)

cv2.circle(img, center, radius, (0,255,0), 2)

cv2.imshow('Enclosing Circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
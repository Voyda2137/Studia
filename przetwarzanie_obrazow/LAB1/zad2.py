import cv2 as cv

img = cv.imread(cv.samples.findFile('pudzian.jpg'))
cv.imshow('Display', img)
klawisz = cv.waitKey(0)
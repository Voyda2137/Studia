import cv2 as cv

img = cv.imread(cv.samples.findFile('pudzian.jpg'))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Display', gray)
klawisz = cv.waitKey(0)
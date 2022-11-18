import cv2 as cv


img = cv.imread(cv.samples.findFile('pudzian3.jpg'))
width = int(img.shape[1] * 1.5) #wczytanie szerokości
height = int(img.shape[0] * 1.5) #wczytanie wysokości
img = cv.resize(img, (width, height))

cv.imshow('Display', img)
klawisz = cv.waitKey(0)
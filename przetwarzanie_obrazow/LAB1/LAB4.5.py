import cv2 as cv
import numpy as np

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)

img = cv.imread(cv.samples.findFile('pudzian.jpg'))

scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)  # zwiększenie szerokości
height = int(img.shape[0] * scale_percent / 100)  # zwiększenie wysokości
dimensions = (width, height)

resized = cv.resize(img, dimensions)
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
sharpened1 = cv.filter2D(src=resized, ddepth=-1, kernel=kernel)
sharpened2 = cv.GaussianBlur(resized, (5, 5), cv.BORDER_DEFAULT)
sharpened3 = cv.medianBlur(resized, 5)

cv.imshow('Display', resized)
cv.imshow('Sharpened', sharpened1)
cv.imshow('Sharpened 2', sharpened2)
cv.imshow('Sharpened 3', sharpened3)


klawisz = cv.waitKey(0)

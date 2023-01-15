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
blur = cv.blur(resized, (9,9))

cv.imshow('Display', resized)
cv.imshow('Blurred', blur)

klawisz = cv.waitKey(0)

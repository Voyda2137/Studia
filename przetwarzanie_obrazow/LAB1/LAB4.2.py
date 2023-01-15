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

median1 = cv.medianBlur(resized, 5)
median2 = cv.medianBlur(resized, 9)
median3 = cv.medianBlur(resized, 11)

cv.imshow('Display', resized)
cv.imshow('Median1', median1)
cv.imshow('Median2', median2)
cv.imshow('Median3', median3)


klawisz = cv.waitKey(0)

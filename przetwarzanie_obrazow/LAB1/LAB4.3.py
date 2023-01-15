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
bilateral1 = cv.bilateralFilter(resized,9,75,75)
bilateral2 = cv.bilateralFilter(resized,9,50,50)
bilateral3 = cv.bilateralFilter(resized,9,25,25)



cv.imshow('Display', resized)
cv.imshow('bilateral1', bilateral1)
cv.imshow('bilateral2', bilateral2)
cv.imshow('bilateral3', bilateral3)



klawisz = cv.waitKey(0)

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

dst1 = cv.GaussianBlur(resized, (5, 5), cv.BORDER_DEFAULT)
dst2 = cv.GaussianBlur(resized, (9, 9), cv.BORDER_DEFAULT)
dst3 = cv.GaussianBlur(resized, (11,11), cv.BORDER_DEFAULT)


cv.imshow('Display', resized)
cv.imshow('Blurred', dst1)
cv.imshow('Blurred2', dst2)
cv.imshow('Blurred3', dst3)


klawisz = cv.waitKey(0)

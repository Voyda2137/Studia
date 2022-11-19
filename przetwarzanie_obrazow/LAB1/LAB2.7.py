import cv2 as cv

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)

img = cv.imread(cv.samples.findFile('pudzian3.jpg'))
width = int(img.shape[1] * 1.5) #wczytanie szerokości
height = int(img.shape[0] * 1.5) #wczytanie wysokości
img = cv.resize(img, (width, height))

cv.imshow('Display', img)
klawisz = cv.waitKey(0)
import cv2 as cv
path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)
img = cv.imread(cv.samples.findFile('pudzian.jpg'))
cv.imshow('Display', img)
klawisz = cv.waitKey(0)
import cv2 as cv


path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)
img = cv.imread(cv.samples.findFile('pudzian.jpg'))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Display', gray)
klawisz = cv.waitKey(0)
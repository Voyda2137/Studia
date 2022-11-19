import cv2 as cv

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)

img = cv.imread(cv.samples.findFile('pudzian.jpg'))
crop = img[50:180, 100:400] #jaka część obrazka ma być wyświetlona jako prostokąt
cv.imshow('Display', crop)
klawisz = cv.waitKey(0)
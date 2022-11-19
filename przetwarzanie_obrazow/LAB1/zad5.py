import cv2 as cv

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)

img = cv.imread(cv.samples.findFile('pudzian.jpg'))
cv.imshow('Oryginalny', img)

font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1
org = (50, 50) #polozenie
color = (255, 0, 0)
img2 = cv.putText(img, 'Zmieniony', org, font, fontScale, color)
cv.imshow('Zmienione', img2)
klawisz = cv.waitKey(0)
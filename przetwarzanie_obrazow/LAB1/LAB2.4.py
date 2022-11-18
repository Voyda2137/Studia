import cv2 as cv

img = cv.imread(cv.samples.findFile('pudzian.jpg'))
crop = img[50:180, 100:400] #jaka część obrazka ma być wyświetlona jako prostokąt
cv.imshow('Display', crop)
klawisz = cv.waitKey(0)
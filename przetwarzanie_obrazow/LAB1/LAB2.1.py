import cv2 as cv
import numpy as np

img = cv.imread(cv.samples.findFile('pudzian.jpg'))
height, width = img.shape[:2] #odczytanie wysokosci i szerokosci zdjecia
translation_matrix = np.float32([ [1,0,70], [0,1,110] ]) #macierz translacji
img_translation = cv.warpAffine(img, translation_matrix, (height, width)) #warpAffine przeprowadza translację zdjęcia
cv.imshow('Display', img_translation)
klawisz = cv.waitKey(0)



import cv2 as cv
import numpy as np
img1 = cv.imread(cv.samples.findFile('pudzian.jpg'))
img2 = cv.imread(cv.samples.findFile('pudzian.jpg'))
img1 = cv.flip(img1, 0) #odbicie w pionie
img2 = cv.flip(img2, 1) #odbicie w poziomie
imgs = np.concatenate((img1, img2), axis=1) #złączenie żeby wyświetlić 2 zdjęcia naraz
cv.imshow('Display', imgs)
klawisz = cv.waitKey(0)
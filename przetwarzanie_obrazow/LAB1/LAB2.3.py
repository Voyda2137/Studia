import cv2 as cv
import numpy as np

def rotate_image(image, degrees):
  image_center = tuple(np.array(image.shape[1::-1]) / 2) #znalezienie środka zdjęcia
  rot_mat = cv.getRotationMatrix2D(image_center, degrees, 1.0) #stworzenie macierzy obrotu
  result = cv.warpAffine(image, rot_mat, image.shape[1::-1]) #obrót zdjęcia
  return result
degrees = 27
img = cv.imread(cv.samples.findFile('pudzian.jpg'))
cv.imshow('Display', rotate_image(img, degrees)) #wywołanie funkcji
klawisz = cv.waitKey(0)
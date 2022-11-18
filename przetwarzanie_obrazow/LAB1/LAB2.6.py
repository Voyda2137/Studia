import cv2 as cv

img = cv.imread(cv.samples.findFile('pudzian3.jpg'))
scale_percent = 50
# width = int(img.shape[1] * scale_percent / 100) #zwiększenie szerokości
# height = int(img.shape[0] * scale_percent / 100) #zwiększenie wysokości
# dimensions = (width, height)
# resized = cv.resize(img, dimensions)
# cv.imshow('Display', resized)


width = int(img.shape[1] / 2) #wczytanie szerokości
height = int(img.shape[0] / 2) #wczytanie wysokości
img = cv.pyrDown(img, dstsize=(width, height))
cv.imshow('Display', img)

klawisz = cv.waitKey(0)
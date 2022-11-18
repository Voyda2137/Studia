import cv2 as cv

img = cv.imread(cv.samples.findFile('pudzian3.jpg'))
width = int(img.shape[1] * 4) #wczytanie szerokości
height = int(img.shape[0] * 4) #wczytanie wysokości
resized = cv.pyrUp(img, (width, height)) #dstsize zwiększa długość i szerokość zdjęcia
cv.imwrite('Pudzianx4-pyrUp.jpg', resized)
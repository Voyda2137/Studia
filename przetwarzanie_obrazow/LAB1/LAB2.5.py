import cv2 as cv
import os

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)

img = cv.imread(cv.samples.findFile('pudzian3.jpg'))

scale_percent = 200
width = int(img.shape[1] * scale_percent / 100)  # zwiększenie szerokości
height = int(img.shape[0] * scale_percent / 100)  # zwiększenie wysokości
dimensions = (width, height)
resized = cv.resize(img, dimensions)
cv.imwrite(os.path.join(path, 'Pudzianx2-resize.jpg'), resized)

scale_percent = 400
width = int(img.shape[1] * scale_percent / 100)  # zwiększenie szerokości
height = int(img.shape[0] * scale_percent / 100)  # zwiększenie wysokości
dimensions = (width, height)
resized = cv.resize(img, dimensions)
cv.imwrite(os.path.join(path, 'Pudzianx4-resize.jpg'), resized)

width = int(img.shape[1] * 2)  # wczytanie szerokości
height = int(img.shape[0] * 2)  # wczytanie wysokości
resized = cv.pyrUp(img, dstsize=(width, height))  # dstsize zwiększa długość i szerokość zdjęcia
cv.imwrite(os.path.join(path, 'Pudzianx2-pyrUp.jpg'), resized)

# width = int(img.shape[1] * 4)  # wczytanie szerokości
# height = int(img.shape[0] * 4)  # wczytanie wysokości
# resized = cv.pyrUp(img, dstsize=(width, height))  # opencv nie pozwala na zwiększenie czterokrotnie obrazu
#cv.imwrite(os.path.join(path, 'Pudzianx4-pyrUp.jpg'), resized)

klawisz = cv.waitKey(0)

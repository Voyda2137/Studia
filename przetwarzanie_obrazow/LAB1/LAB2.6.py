import cv2 as cv
import os 

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)

img = cv.imread(cv.samples.findFile('pudzian3.jpg'))
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)  # zmniejszenie szerokości
height = int(img.shape[0] * scale_percent / 100)  # zmniejszenie wysokości
dimensions = (width, height)
resized = cv.resize(img, dimensions)
cv.imwrite(os.path.join(path, 'Pudzianx05-resize.jpg'), resized)

scale_percent = 25
width = int(img.shape[1] * scale_percent / 100)  # zmniejszenie szerokości
height = int(img.shape[0] * scale_percent / 100)  # zmniejszenie wysokości
dimensions = (width, height)
resized = cv.resize(img, dimensions)
cv.imwrite(os.path.join(path, 'Pudzianx025-resize.jpg'), resized)

width = int(img.shape[1] * 0.5)  # wczytanie szerokości
height = int(img.shape[0] * 0.5)  # wczytanie wysokości
resized = cv.pyrDown(img, dstsize=(width, height))  # dstsize zminiejsza długość i szerokość zdjęcia
cv.imwrite(os.path.join(path, 'Pudzianx05-pyrDown.jpg'), resized)

# width = int(img.shape[1] * 0.25)  # wczytanie szerokości
# height = int(img.shape[0] * 0.25)  # wczytanie wysokości
# resized = cv.pyrDown(img, dstsize=(width, height))  # opencv nie pozwala na zmniejszenie czterokrotnie obrazu
# cv.imwrite(os.path.join(path, 'Pudzianx025-pyrDown.jpg'), resized)

klawisz = cv.waitKey(0)
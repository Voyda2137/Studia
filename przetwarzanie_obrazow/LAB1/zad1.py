import cv2 as cv
cv.samples.addSamplesDataSearchPath("C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1")
img = cv.imread(cv.samples.findFile('png.png'))
cv.imwrite('png2.png', img)



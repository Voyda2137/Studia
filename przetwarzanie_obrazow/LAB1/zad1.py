import cv2 as cv
import os
path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)
img = cv.imread(cv.samples.findFile('png.png'))
cv.imwrite(os.path.join(path, 'png2.png'), img)



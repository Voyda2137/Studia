import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)


img = cv.imread(cv.samples.findFile('green.jpg'))
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
background_img = cv.imread(cv.samples.findFile('pudzian.jpg'))
u_green = np.array([104, 153, 70])
l_green = np.array([30, 30, 0])

scale_percent = 10
width = int(img.shape[1] * scale_percent / 100)  # zwiększenie szerokości
height = int(img.shape[0] * scale_percent / 100)  # zwiększenie wysokości
dimensions = (width, height)
resized = cv.resize(img, dimensions)

image_copy = np.copy(resized)
image_copy = cv.cvtColor(image_copy, cv.COLOR_BGR2RGB)
mask = cv.inRange(image_copy, l_green, u_green)
plt.imshow(mask, cmap='gray')
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
plt.imshow(masked_image)
crop_background = background_img[0:403, 0:302]

crop_background[mask == 0] = [0, 0, 0]

plt.imshow(crop_background)
final_image = crop_background + masked_image
cv.imshow('dsa',final_image)
plt.show()

klawisz = cv.waitKey(0)
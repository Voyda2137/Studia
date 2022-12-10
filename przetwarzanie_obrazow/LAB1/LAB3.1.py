import cv2

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv2.samples.addSamplesDataSearchPath(path)

img = cv2.imread(cv2.samples.findFile('ja.jpg'))

# zdefiniowanie dolnego i górnego zielonego
lower_green = (0, 100, 0)
upper_green = (100, 255, 130)

# Maska z tylko zielonym kolorem
mask = cv2.inRange(img, lower_green, upper_green)

# Zamiana zielonego na białe pixele
img[mask > 0] = (255, 255, 255)

replacement_bg = cv2.imread(cv2.samples.findFile('pudzior.jpg'))


# SKopiowane tła na zdjęcie z użyciem maski żeby skopowiać tylko pixele gdzie usuwany jest zielony
img[mask > 0] = replacement_bg[mask > 0]

cv2.imwrite('nowe_tlo.jpg', img)

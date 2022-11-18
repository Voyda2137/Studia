import cv2 as cv

jpg = cv.imread(cv.samples.findFile('pudzian.jpg'))
png = cv.imread(cv.samples.findFile('png.png'))
bmp = cv.imread(cv.samples.findFile('bmp.bmp'))
gif = cv.imread(cv.samples.findFile('gif.gif'))
ret, image = gif.read()
cv.imshow('jpg', jpg)
cv.imshow('png', png)
cv.imshow('bmp', bmp)
cv.imshow('gif', gif) #to nie dziala i tak ma byc

klawisz = cv.waitKey(0)
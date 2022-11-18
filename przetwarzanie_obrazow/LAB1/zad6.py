import cv2 as cv

img = cv.imread(cv.samples.findFile('pudzian.jpg'))
cv.imshow('Oryginalny', img)

start_point = (5, 5)
end_point = (220, 220)
color = (255, 0, 0)

radius = 20
center_coordinates = (120, 50)

img2 = cv.rectangle(img, start_point, end_point, color)
cv.imshow('kwadrat', img2)
img3 = cv.circle(img, center_coordinates, radius, color)
cv.imshow('kolko', img3)

start_point = (5, 5)
end_point = (220, 400)
color = (255, 0, 0)

img4 = cv.line(img, start_point, end_point, color)
cv.imshow('kreska', img4)

klawisz = cv.waitKey(0)
import cv2 as cv
import numpy as np

path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv.samples.addSamplesDataSearchPath(path)

video = cv.VideoCapture(cv.samples.findFile("greenfilmik.MOV"))
image = cv.imread(cv.samples.findFile("pudzian.jpg"))

def create_mask_with_threshold(frame):
    # split the the B, G and R channels
    b, g, r = cv.split(frame)

    # create the threshold
    _, mask = cv.threshold(g, 245, 255, cv.THRESH_BINARY_INV)

    # De-noise the threshold to get a cleaner mask
    mask = cv.erode(mask, cv.getStructuringElement(cv.MORPH_RECT, (9, 9)))

    return mask
def replace_background(frame, bg, mask):
    # if the pixel on threshold is background then make it white
    frame[mask == 0] = 255

    # if the pixel on threshold is not background then make it black
    bg[mask != 0] = 255

    # combine both images into frame
    return cv.bitwise_and(bg, frame)
while True:
 
    ret, frame = video.read()
 
    frame = cv.resize(frame, (640, 480))
    image = cv.resize(image, (640, 480))
 
 
    u_green = np.array([104, 153, 70])
    l_green = np.array([30, 30, 0])
 
    mask = cv.inRange(frame, l_green, u_green)
    res = cv.bitwise_and(frame, frame, mask = mask)
 
    f = frame - res
    f = np.where(f == 0, image, f)
 
    cv.imshow("video", frame)
    cv.imshow("mask", f)
 
    if cv.waitKey(25) == 27:
        break
 
video.release()
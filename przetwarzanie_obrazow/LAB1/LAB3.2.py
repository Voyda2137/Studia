import cv2
import numpy as np
path = "C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\przetwarzanie_obrazow\\LAB1"
cv2.samples.addSamplesDataSearchPath(path)

video = cv2.VideoCapture(cv2.samples.findFile("greenfilmik.MOV"))
replacement_bg = cv2.imread(cv2.samples.findFile("pudzian.jpg"))

# zdefiniowanie dolnego i górnego zielonego
lower_green = (0, 100, 0)
upper_green = (100, 255, 130)


while True:
  # Odczyt klatek
  success, frame = video.read()
  frame = cv2.resize(frame, (640, 480))
  frame=cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
  frame=cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
  replacement_bg = cv2.resize(replacement_bg, (640, 480))
  # Jeśli skończyły się klatki break z pętli
  if not success:
    break

  # Maska zawierająca tylko zielony
  mask = cv2.inRange(frame, lower_green, upper_green)

  # zamiana zielonego na białe pixele
  frame[mask > 0] = (255, 255, 255)

  # resize zdjęcia żeby pasowało rozmiarem do klatki
  replacement_bg = cv2.resize(replacement_bg, (frame.shape[1], frame.shape[0]))
# SKopiowane tła na klatkę z użyciem maski żeby skopowiać tylko pixele gdzie usuwany jest zielony
  frame[mask > 0] = replacement_bg[mask > 0]

  cv2.imshow('frame', frame)

  # Bez tego program nie działa
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video.release()

cv2.destroyAllWindows()
from time import time
import numpy as np 
import cv2,time

video = cv2.VideoCapture(0)
address = "http://192.168.0.137:8080/video"
video.open(address)


while(video.isOpened()):
    ret, frame = video.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(type(frame))

        cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()




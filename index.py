import imp
import numpy as np
from PIL import ImageGrab
import cv2
import time


t = time.process_time()
print(t)

while True:
    window = np.array(ImageGrab.grad(bbox=(10, 10, 810, 720)))

    print("Frame time: " + str(time.process_time() - t))
    t = time.process_time()
    im = cv2.cvtColor(window, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize = 1)
    sobely = cv2.Sobel(im, cv2.CV_32F, 0, 1, ksize = 1)
    sob = (sobelx + sobely)

    cv2.imshow("window_new", sob)
    if cv2.waitKey(30) == ord("q"):
        cv2.destroyAllWindows()
        break

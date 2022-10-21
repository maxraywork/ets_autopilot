import imp
import numpy as np
from PIL import ImageGrab
import cv2
import time


t = time.process_time()
print(t)

while True:
    window = np.array(ImageGrab.grad(bbox = (10, 10, 810, 720)))

    print("Frame time: " + str(time.process_time() - t))
    t = time.process_time()

    cv2.imshow("window_new", cv2.cvtColor(window, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(30) == ord("q"):
        cv2.destroyAllWindows()
        break
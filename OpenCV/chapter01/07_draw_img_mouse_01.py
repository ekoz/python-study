# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/22 23:12
import cv2
import numpy as np


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
# double click to draw a circle
cv2.setMouseCallback("image", draw_circle)

while 1:
    cv2.imshow("image", img)
    # 0xFF == 27  equals press Esc
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

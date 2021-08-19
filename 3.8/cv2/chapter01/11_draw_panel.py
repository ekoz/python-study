# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/23 21:31
import cv2
import numpy as np


def nothing(x):
    pass


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("image")

# create trackbars for color change
# 第一个参数是滑动条的名字
# 第二个参数是滑动条被放置窗口的名字
# 第三个参数是滑动条的默认位置。第四个参数是滑动条的最大值
# 第五个函数是回调函数，每次滑动条的滑动都会调用回调函数。回调函数通常都会含有一个默认参数，就是滑动条的位置。在本例中这个函数不用做任何事情，我们只需要 pass 就可以了。
cv2.createTrackbar("R", "image", 255, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

# create switch for ON/OFF functionality
switch = "0 : OFF \n1 : ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while 1:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    # ESC
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/21 17:03
import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 1)

# 画一个正方形
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 1)

# 画一个圆形
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 画一个椭圆形
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# 画一个多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))

# 写文本
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("draw", img)

cv2.waitKey()

cv2.destroyAllWindows()

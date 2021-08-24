# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/23 22:15
import cv2
import numpy as np

img = cv2.imread("../data/messi5.jpg")

# 获取图片中的一个区域
width, height = (180, 240)
x1, y1 = (225, 10)
x2, y2 = (x1 + width, y1 + height)
# img[rows:columns] 行数:列数
# 竖直方向起始像素点由y1到y2，然后是水平方向起始像素点由x1到x2
ball = img[y1:y2, x1:x2]

# cv2.imshow("ball", ball)

# 将该区域复制到固定区域
b1, c1 = (430, 10)
b2, c2 = (b1 + width, c1 + height)
# cv2.imshow("tmp", img[c1:c2, b1:b2])
img[c1:c2, b1:b2] = ball

img = cv2.imshow("messi", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

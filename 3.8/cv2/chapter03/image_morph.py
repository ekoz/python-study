# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/25 20:31
import cv2
import numpy as np

img = cv2.imread("../data/erode.png")

# (5, 5) 该参数配合腐蚀迭代次数一起试用
kernel = np.ones((5, 5), np.uint8)
# 先腐蚀，再膨胀
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)

# 先膨胀，再腐蚀
close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)

res = np.hstack((img, open_img, close_img))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

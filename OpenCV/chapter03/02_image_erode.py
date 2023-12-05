# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/25 19:44
import cv2
import numpy as np

# 腐蚀操作
img = cv2.imread("../data/erode.png")

# (5, 5) 该参数配合腐蚀迭代次数一起试用
kernel = np.ones((5, 5), np.uint8)
# 迭代次数，多搞几次，全部都腐蚀没了，可以通过调整该参数观察
erosion = cv2.erode(img, kernel, iterations=2)


kernel2 = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(erosion, kernel2, iterations=3)

res = np.hstack((img, erosion, dilate))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

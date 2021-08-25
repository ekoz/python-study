# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/25 20:31
import cv2
import numpy as np

img = cv2.imread("../data/cycle.png")

# (5, 5) 该参数配合腐蚀迭代次数一起试用
kernel = np.ones((5, 5), np.uint8)
# 迭代次数，多搞几次，全部都腐蚀没了，可以通过调整该参数观察
dilate1 = cv2.dilate(img, kernel, iterations=1)
dilate2 = cv2.dilate(img, kernel, iterations=2)
dilate3 = cv2.dilate(img, kernel, iterations=4)
dilate4 = cv2.dilate(img, kernel, iterations=8)
dilate5 = cv2.dilate(img, kernel, iterations=16)

# 梯度运算，膨胀减去腐蚀后的效果，月环食
gradient_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

res = np.hstack((dilate1, dilate2, dilate3, dilate4, dilate5, gradient_img))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

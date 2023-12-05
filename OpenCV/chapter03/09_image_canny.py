# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/29 22:37
import cv2
import numpy as np

# Canny 边缘检测
# 1、使用高斯滤波器，以平滑图像，滤除噪音
# 2、计算图像中每个像素点的梯度强度和方向
# 3、应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应
# 4、应用双阈值（Double-Threshold）检测来确定真实和潜在的边缘
# 5、通过抑制孤立的弱边缘最终完成边缘检测

img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_GRAYSCALE)

v1 = cv2.Canny(img, 80, 150)
v2 = cv2.Canny(img, 50, 100)

vv1 = cv2.Canny(img, 120, 250)
vv2 = cv2.Canny(img, 50, 100)

res = np.hstack((v1, v2, vv1))

cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

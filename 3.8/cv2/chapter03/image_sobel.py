# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/26 21:27
import cv2
import numpy as np

# Sobel 算子

img = cv2.imread("../data/cycle.png", cv2.IMREAD_GRAYSCALE)

# ddepth 图像的深度
# dx 和 dy 分别标识水平和竖直方向
# ksize 是 Sobel算子的大小，ksize=3 表示是一个3*3的矩阵，也可以写作（3, 3）
sobelx_img = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

cv2.imshow("Original", img)
cv2.waitKey()

# 白到黑是正数，黑到白是负数，所有的负数会被截断为0，所以要取绝对值
sobelx_img2 = cv2.convertScaleAbs(sobelx_img)

sobely_img = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely_img2 = cv2.convertScaleAbs(sobely_img)

res = np.hstack((sobelx_img, sobelx_img2, sobely_img, sobely_img2))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

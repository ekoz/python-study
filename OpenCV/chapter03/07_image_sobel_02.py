# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/26 21:27
import cv2
import numpy as np

# 一个完整的 Sobel 算子用例

img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_GRAYSCALE)

sobelx_img = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx_img = cv2.convertScaleAbs(sobelx_img)

sobely_img = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely_img = cv2.convertScaleAbs(sobely_img)

sobelxy_img = cv2.addWeighted(sobelx_img, 0.5, sobely_img, 0.5, 0)

# 不建议直接计算，可通过对比查看效果
sobelxy_img2 = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
sobelxy_img2 = cv2.convertScaleAbs(sobelxy_img2)

res = np.hstack((img, sobelxy_img, sobelxy_img2))
cv2.imshow("res", res)

cv2.waitKey()
cv2.destroyAllWindows()

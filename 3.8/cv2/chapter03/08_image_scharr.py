# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/29 22:37
import cv2
import numpy as np

# Canny 边缘检测

img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_GRAYSCALE)

sobelx_img = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx_img = cv2.convertScaleAbs(sobelx_img)
sobely_img = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely_img = cv2.convertScaleAbs(sobely_img)
sobelxy_img = cv2.addWeighted(sobelx_img, 0.5, sobely_img, 0.5, 0)

scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((sobelxy_img, scharrxy, laplacian))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

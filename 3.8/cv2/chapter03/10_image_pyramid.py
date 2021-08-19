# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/9/2 19:56
import cv2
import numpy as np

img = cv2.imread("../data/dog-1.jpg")


# 高斯金字塔
pyr_up_img = cv2.pyrUp(img)
pyr_down_img = cv2.pyrDown(pyr_up_img)

print(pyr_up_img.shape)

cv2.imshow("res0", img)
cv2.imshow("res1", pyr_up_img)
cv2.imshow("res2", pyr_down_img)
cv2.waitKey()
cv2.destroyAllWindows()

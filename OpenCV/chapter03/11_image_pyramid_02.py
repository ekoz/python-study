# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/9/2 19:56
import cv2
import numpy as np

img = cv2.imread("../data/dog-1.jpg")

# 拉普拉斯金字塔 L = G -PyrUp(PyrDown(G))
pyr_img = img - cv2.pyrUp(cv2.pyrDown(img))

print(pyr_img.shape)

cv2.imshow("res0", img)
cv2.imshow("res1", pyr_img)
cv2.waitKey()
cv2.destroyAllWindows()

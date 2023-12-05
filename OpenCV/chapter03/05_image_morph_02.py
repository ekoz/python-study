# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/25 21:04
import cv2
import numpy as np

# 礼帽和黑帽
img = cv2.imread("../data/erode.png")

# (5, 5) 该参数配合腐蚀迭代次数一起试用
kernel = np.ones((5, 5), np.uint8)
# 礼帽：原始值-开运算结果
tophat_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽：闭运算结果-原始值
black_img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

res = np.hstack((img, tophat_img, black_img))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

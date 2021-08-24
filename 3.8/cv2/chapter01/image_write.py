# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/19 20:42

import cv2
from matplotlib import pyplot as plt

# 彩色图 cv2.IMREAD_COLOR
# 灰度图 cv2.IMREAD_GRAYSCALE
img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("../data/dog-gray.jpg", img)

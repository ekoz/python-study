# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/23 22:01
import cv2
import numpy as np

img = cv2.imread("../data/dog-2.jpg")
# 获取像素值
px = img[100, 100]
print(px)  # [136 169 195]

blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

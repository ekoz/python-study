# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/23 22:08
import cv2
import numpy as np

img = cv2.imread("../data/messi5.jpg")
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

# 图像的属性包括：行，列，通道，图像数据类型，像素数目等img.shape 可以获取图像的形状。他的返回值是一个包含行数，列数，通道数的元组。
print(img.shape)  # (434, 650, 3)

# 如果图像是灰度图，返回值仅有行数和列数。所以通过检查这个返回值就可以知道加载的是灰度图还是彩色图
print(img.size, img.dtype)  # 返回的是图像的数据类型

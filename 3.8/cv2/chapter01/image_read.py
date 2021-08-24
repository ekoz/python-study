# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/19 20:42

import numpy as np
import cv2
from matplotlib import pyplot as plt

# 彩色图 cv2.IMREAD_COLOR
# 灰度图 cv2.IMREAD_GRAYSCALE
img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_COLOR)
r, g, b = cv2.split(img)
print(b)
print(b.shape)
img2 = img.copy()
# 去掉 img2 的 Red 和 Green，保留 Blue
img2[:, :, 0] = 0
img2[:, :, 1] = 0
# plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.subplot(121), plt.imshow(img, "gray", interpolation="bicubic"), plt.title("Source")
plt.subplot(122), plt.imshow(img2), plt.title("Blue")
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

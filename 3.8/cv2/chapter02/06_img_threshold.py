# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/24 23:27

import cv2
from matplotlib import pyplot as plt

# 阈值处理用例
img_gray = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_GRAYSCALE)

thresh_val, max_val = (127, 255)

ret, thresh1 = cv2.threshold(img_gray, thresh_val, max_val, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img_gray, thresh_val, max_val, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img_gray, thresh_val, max_val, cv2.THRESH_TOZERO)
ret, thresh4 = cv2.threshold(img_gray, thresh_val, max_val, cv2.THRESH_TOZERO_INV)
ret, thresh5 = cv2.threshold(img_gray, thresh_val, max_val, cv2.THRESH_TRUNC)

titles = [
    "Original",
    "THRESH_BINARY",
    "THRESH_BINARY_INV",
    "THRESH_TOZERO",
    "THRESH_TOZERO_INV",
    "THRESH_TRUNC",
]
imgs = [img_gray, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(imgs[i], "gray"), plt.title(titles[i])

plt.show()

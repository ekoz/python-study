# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/10/17 16:02

import cv2
import numpy as np

# 读取图片
image_path = "../data/202410171608.jpg"
image = cv2.imread(image_path)


# 增加对比度
def increase_contrast(img, alpha=1.2):
    minimum = np.min(img)
    maximum = np.max(img)
    img_scaled = alpha * (img - minimum) / (maximum - minimum)
    img_scaled = img_scaled * 255 / np.max(img_scaled)
    return np.uint8(img_scaled)


# 增加线条强度
def enhance_lines(img, factor=1.5):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_enhanced = cv2.addWeighted(img_gray, 1 + factor, img_blurred, 0, 0)
    return img_enhanced


# 应用增加对比度和强度的函数
image_contrasted = increase_contrast(image, 1.2)
# image_lines_blackened = enhance_lines(image_contrasted)

# 显示图片
cv2.imshow("Original", image)
cv2.imshow("Contrasted", image_contrasted)
# cv2.imshow('Lines Blackened', image_lines_blackened)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(image_path + "_image_contrasted.jpg", image_contrasted)

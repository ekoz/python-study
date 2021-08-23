# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/19 20:42

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_COLOR)
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/9/2 20:30

import cv2
import numpy as np


img = cv2.imread("../data/cycle.png")

# mode：轮廓检测模式
# RETR_EXTERNAL：只检索最外面的轮廓
# RETR_LIST：检索所有轮廓，并将结果保存至链表中
# RETR_CCOMP：检索所有轮廓，并将他们组织为两层，顶层是各部分的外部边界，第二层是空洞的边界
# RETR_TREE：检索所有轮廓，并重构嵌套轮廓的整个层次

# method：轮廓逼近方法
# CHAIN_APPROX_NONE：以Freeman链码的方式输出轮廓，所有其他方法输出多边形（顶点的序列）
# CHAIN_APPROX_SIMPLE：压缩水平的，垂直和斜的部分，只保留他们的终点部分


# 为了使准确率更高，我们使用二值图像
gary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gary_img, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# print(binary)
# print(contours)
print(contours[0])
print(cv2.contourArea(contours[0]))


# 如果不用 img.copy()，会改变原图片
draw_img = img.copy()
# https://stackoverflow.com/questions/55854810/opencv-version-4-1-0-drawcontours
# 第三个参数，传入-1 是指画所有轮廓
# 第五个参数是画轮廓的粗细
draw_img2 = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 2)

res = np.hstack((img, draw_img2))
cv2.imshow("res", res)
cv2.waitKey()
cv2.destroyAllWindows()

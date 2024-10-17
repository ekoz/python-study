# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/10/14 16:16

from PIL import Image
import numpy as np
import cv2


# 图片转成黑白图
def convert_to_black_and_white(image_path):
    with Image.open(image_path) as image:
        image = image.convert("L")
        image.save(image_path + "_out.jpg")


# 降噪
def denoise(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    denoised_img = cv2.medianBlur(img, 3)
    cv2.imshow("Denoised Image", denoised_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(image_path + "_denoised_image.jpg", denoised_img)


convert_to_black_and_white("../data/202410171548-shuxue.jpeg")

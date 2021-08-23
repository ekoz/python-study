# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/19 10:26
import cv2
import numpy as np
import skimage
from skimage.util.dtype import convert

# 阅读图像
# cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。
# cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
# cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道
img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_COLOR)
cv2.imshow("dog", img)
cv2.waitKey()

# 2.添加噪声
# 方法1：用第三方工具添加噪声
# - 'gaussian'  Gaussian-distributed additive noise.
# - 'localvar'  Gaussian-distributed additive noise, with specified
#               local variance at each point of `image`.
# - 'poisson'   Poisson-distributed noise generated from the data.
# - 'salt'      Replaces random pixels with 1.
# - 'pepper'    Replaces random pixels with 0 (for unsigned images) or
#               -1 (for signed images).
# - 's&p'       Replaces random pixels with either 1 or `low_val`, where
#               `low_val` is 0 for unsigned images or -1 for signed
#               images.
# - 'speckle'   Multiplicative noise using out = image + n*image, where
#               n is Gaussian noise with specified mean & variance.
noise_img = skimage.util.random_noise(img, mode="speckle")

cv2.imshow("dog2", noise_img)


# 方法2：用numpy生成噪声
def add_noise(p_img):
    p_img = np.multiply(p_img, 1.0 / 255, dtype=np.float64)
    mean, var = 0, 0.01
    noise = np.random.normal(mean, var ** 0.5, p_img.shape)
    p_img = convert(p_img, np.floating)
    out = p_img + noise
    return out


noise_img3 = add_noise(img).astype(np.float32)
gray_img = cv2.cvtColor(noise_img3, cv2.COLOR_BGR2GRAY)
cv2.imshow("dog3", noise_img3)
# > Unsupported depth of input image:
# >     'VDepth::contains(depth)'
# > where
# >     'depth' is 6 (CV_64F)
# https://stackoverflow.com/questions/55128386/python-opencv-depth-of-image-unsupported-cv-64f
# https://blog.csdn.net/SpadgerZ/article/details/103297962
# opencv只支持float32的图像显示和操作，然后float64是numpy的数据类型，opencv中不支持。改成np.float32即可
cv2.imshow("dog31", gray_img)


# 图像去噪
# 方法1：用第三方工具去噪
noise_img_dog = cv2.imread("../data/dog-1_noise.png")

denoise_img1 = cv2.medianBlur(noise_img_dog, ksize=5)
cv2.imshow("denoise_img1", denoise_img1)

denoise_img2 = cv2.fastNlMeansDenoising(noise_img_dog)
cv2.imshow("denoise_img2", denoise_img2)

# denoise_img3 = cv2.GaussianBlur(noise_img_dog, ksize=3, sigmaX=(-1, 1))
# cv2.imshow("denoise_img3", denoise_img3)


def compute_pixel_value(p_img, i, j, ksize, channel):
    h_begin = max(0, i - ksize // 2)
    h_end = min(p_img.shape[0], i + ksize // 2)
    w_begin = max(0, j - ksize // 2)
    w_end = min(p_img.shape[1], j + ksize // 2)
    return np.median(p_img[h_begin:h_end, w_begin:w_end, channel])


def denoise(p_img, ksize):
    output = np.zeros(p_img.shape)
    for i in range(p_img.shape[0]):
        for j in range(p_img.shape[1]):
            output[i, j, 0] = compute_pixel_value(p_img, i, j, ksize, 0)
            output[i, j, 1] = compute_pixel_value(p_img, i, j, ksize, 1)
            output[i, j, 2] = compute_pixel_value(p_img, i, j, ksize, 2)
    return output


# denoise_img4 = denoise(noise_img_dog, 1)
# cv2.imshow("denoise_img4", denoise_img4)

cv2.waitKey()

cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/19 10:26
import cv2
import numpy as np
import skimage
from skimage.util.dtype import convert
from matplotlib import pyplot as plt

# 阅读图像
# cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。
# cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
# cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道
img = cv2.imread("../data/dog-1.jpg", cv2.IMREAD_COLOR)
plt.subplot(231), plt.imshow(img), plt.title("Original")

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
plt.subplot(232), plt.imshow(noise_img), plt.title("skimage_random_noise")


# 方法2：用numpy生成噪声
def add_noise(p_img):
    p_img = np.multiply(p_img, 1.0 / 255, dtype=np.float64)
    mean, var = 0, 0.01
    noise = np.random.normal(mean, var ** 0.5, p_img.shape)
    p_img = convert(p_img, np.floating)
    out = p_img + noise
    return out


noise_img3 = add_noise(img).astype(np.float32)
plt.subplot(233), plt.imshow(noise_img3), plt.title("np_random_noise")

gray_img = cv2.cvtColor(noise_img3, cv2.COLOR_BGR2GRAY)
# > Unsupported depth of input image:
# >     'VDepth::contains(depth)'
# > where
# >     'depth' is 6 (CV_64F)
# https://stackoverflow.com/questions/55128386/python-opencv-depth-of-image-unsupported-cv-64f
# https://blog.csdn.net/SpadgerZ/article/details/103297962
# opencv只支持float32的图像显示和操作，然后float64是numpy的数据类型，opencv中不支持。改成np.float32即可
plt.subplot(234), plt.imshow(gray_img), plt.title("gray_img")


# 图像去噪
# 方法1：用第三方工具去噪
noise_img_dog = cv2.imread("../data/dog-1_noise.png")
plt.subplot(235), plt.imshow(noise_img_dog), plt.title("noise_img_dog")

# 均值滤波
# 3*3的矩阵值之和，然后除以9，求平均值
# cv2.blur(noise_img_dog, (3, 3))

# 方框滤波
# 和均值滤波类似，可以选择归一化操作
# cv2.boxFilter(noise_img_dog, -1, (3, 3), normalize=True)

# 中值滤波
# 将矩阵中的数字由小到大排列，取中间数
median_blur_img = cv2.medianBlur(noise_img_dog, ksize=5)
plt.subplot(236), plt.imshow(median_blur_img), plt.title("medianBlur")

fastNlMeansDenoising_img = cv2.fastNlMeansDenoising(noise_img_dog)
# plt.subplot(236), plt.imshow(fastNlMeansDenoising_img), plt.title(
#     "fastNlMeansDenoising"
# )

# 高斯滤波
# 离像素点越近的，关系越密切，影响越大
gaussian_blur_img = cv2.GaussianBlur(noise_img_dog, (5, 5), 1)
# plt.subplot(235), plt.imshow(gaussian_blur_img), plt.title("GaussianBlur")


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
plt.show()

titles = [
    "noise_img_dog",
    "median_blur_img",
    "gaussian_blur_img",
    "fastNlMeansDenoising_img",
]
imgs = [noise_img_dog, median_blur_img, gaussian_blur_img, fastNlMeansDenoising_img]

for i in range(len(titles)):
    plt.subplot(2, 2, i + 1), plt.imshow(imgs[i]), plt.title(titles[i])
plt.show()

# res = np.hstack(
#     (noise_img_dog, median_blur_img, gaussian_blur_img, fastNlMeansDenoising_img)
# )
# cv2.imshow("list", res)
# cv2.waitKey()
# cv2.destroyAllWindows()

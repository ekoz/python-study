# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/5 17:48

from PIL import Image, ImageEnhance
import os
import time


# 将指定文件夹下的所有文件转成黑白并增强亮度
def convert_to_black_and_white(folder_path):
    if os.path.isdir(folder_path):
        result_path = os.path.dirname(folder_path) + "/results"
        if not os.path.isdir(result_path):
            os.mkdir(result_path)
        for image_name in os.listdir(folder_path):
            image_path = folder_path + "/" + image_name
            with Image.open(image_path) as image:
                image = image.convert("L")
                # 创建一个对比度增强器
                enhancer = ImageEnhance.Contrast(image)
                # 应用对比度增强
                img_enhanced = enhancer.enhance(1.5)
                img_enhanced.save(
                    result_path + "/" + image_name + "_" + str(time.time()) + "_out.jpg"
                )
    print("执行完毕，请查看文件")


convert_to_black_and_white("../data/asserts")

# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/20 18:25
# 人像修复，输入一张包含人像的图像，算法会对图像中的每一个检测到的人像做修复和增强，
# 对图像中的非人像区域采用RealESRNet做两倍的超分辨率，最终返回修复后的完整图像。
# https://modelscope.cn/models/iic/cv_gpen_image-portrait-enhancement

import cv2
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys
import time


model_path_offline = "C:\\Users\\zhanzhao\\.cache\\modelscope\\hub\\damo\\cv_gpen_image-portrait-enhancement"
model_path = "damo/cv_gpen_image-portrait-enhancement"


portrait_enhancement = pipeline(Tasks.image_portrait_enhancement, model=model_path)
result = portrait_enhancement("data/assets/07_result.png_1.png")
cv2.imwrite(
    "data/output/09_result_{}.png".format(time.time()), result[OutputKeys.OUTPUT_IMG]
)
print("finished")

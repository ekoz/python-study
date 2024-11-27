# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/21 14:25
# 人像增强模型会把背景图也处理，有的图片会产生失真，这里主要是尝试只将人像增强，美肤，背景保留原图，避免过度失真

import time

import cv2
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from PIL import Image
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

origin_img = "./data/assets/07_result.png"
result_img = "./data/output/03_result_{}.png".format(time.time())

# 人像抠图 pipeline
portrait_matting = pipeline(Tasks.portrait_matting, model="damo/cv_unet_image-matting")

# 人像增强 pipeline
portrait_enhancement = pipeline(
    Tasks.image_portrait_enhancement, model="damo/cv_gpen_image-portrait-enhancement"
)

# 人像美肤 pipeline
skin_retouching = pipeline(Tasks.skin_retouching, model="damo/cv_unet_skin-retouching")

# 1. 进行人像增强
image_enhancement_result = portrait_enhancement(origin_img)
# 2. 进行人像美肤
image_skin_result = skin_retouching(image_enhancement_result[OutputKeys.OUTPUT_IMG])
# 3. 抠出人像
image_matting_result = portrait_matting(image_skin_result[OutputKeys.OUTPUT_IMG])

cv2.imwrite(result_img, image_matting_result[OutputKeys.OUTPUT_IMG])

# 4. 将抠出来的人像贴到原图上
# 底图背景
layer1 = Image.open(origin_img).convert("RGBA")
# mask
layer2 = Image.open(result_img).convert("RGBA")

# layer1和layer2要相同大小，否则需resize
layer1 = layer1.resize(layer2.size)

# 合成的image
final = Image.new("RGBA", layer1.size)

final = Image.alpha_composite(final, layer1)
final = Image.alpha_composite(final, layer2)

# 5. 保存合并后的图片
final = final.convert("RGB")
final.save(result_img)

logging.info("图片处理完毕")

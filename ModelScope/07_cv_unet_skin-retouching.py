# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/20 17:50
# 基于混合图层的高清人像美肤模型
# https://modelscope.cn/models/iic/cv_unet_skin-retouching

import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import time


model_path_offline = (
    "C:\\Users\\zhanzhao\\.cache\\modelscope\\hub\\damo\\cv_unet_skin-retouching"
)
model_path = "damo/cv_unet_skin-retouching"

skin_retouching = pipeline(Tasks.skin_retouching, model=model_path)
result = skin_retouching("./data/assets/skin_retouching_examples.jpg")
cv2.imwrite(
    "data/output/07_result_{}.png".format(time.time()), result[OutputKeys.OUTPUT_IMG]
)

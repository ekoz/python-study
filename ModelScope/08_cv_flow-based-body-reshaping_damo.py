# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/20 18:22
# 基于光流的人体美型(FBBR)，如果图片中没有检测到人体，则不做任何处理，这个大模型帮我们实现了
# https://modelscope.cn/models/iic/cv_flow-based-body-reshaping_damo

import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import time


model_path_offline = "C:\\Users\\zhanzhao\\.cache\\modelscope\\hub\\damo\\cv_flow-based-body-reshaping_damo"
model_path = "damo/cv_flow-based-body-reshaping_damo"

image_body_reshaping = pipeline(Tasks.image_body_reshaping, model=model_path)
image_path = "data/assets/07_result.png"
result = image_body_reshaping(image_path)

cv2.imwrite(
    "data/output/08_result_{}.png".format(time.time()), result[OutputKeys.OUTPUT_IMG]
)
print("finished!")

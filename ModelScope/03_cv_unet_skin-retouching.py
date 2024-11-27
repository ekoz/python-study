# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/27 16:22
# 基于混合图层的高清人像美肤模型
# https://modelscope.cn/models/iic/cv_unet_skin-retouching
# 遍历指定目录下的图片，然后进行批量人像美肤，将处理过的图片放在该目录下一个时间戳生成的目录里

import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import datetime
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

folder_path = '目标目录路径，如：D:\\Images'
folder_path = 'D:\\Images\\test'

target_path = os.path.join(folder_path, datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

if not os.path.exists(target_path):
    os.mkdir(target_path)

model_path = "damo/cv_unet_skin-retouching"

skin_retouching = pipeline(Tasks.skin_retouching, model=model_path)

for img_path in os.listdir(folder_path):
    full_path = os.path.join(folder_path, img_path)
    if os.path.isfile(full_path):
        result = skin_retouching(full_path)
        cv2.imwrite(
            target_path + '/' + img_path, result[OutputKeys.OUTPUT_IMG]
        )

logging.info('图片处理完毕')

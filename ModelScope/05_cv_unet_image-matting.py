# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2023/12/7 17:40
# 用达摩院的模型来处理，离线验证通过
# https://github.com/modelscope/modelscope/blob/master/README_zh.md
# 还需要安装 tensorflow 和 torch，直接在 conda 环境中 pip install 即可
# BSHM人像抠图，人像抠图对输入含有人像的图像进行处理，无需任何额外输入，实现端到端人像抠图，输出四通道人像抠图结果
# https://modelscope.cn/models/damo/cv_unet_image-matting/summary
import time

import cv2
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline

# 首次需要下载离线模型，也可以直接进入上面的 model summary 页面下载，可以指定 cache_dir
# from modelscope.hub.snapshot_download import snapshot_download
# model_path = snapshot_download('damo/cv_unet_image-matting')
# C:/Users/zhanzhao/.cache/modelscope/hub/damo/cv_unet_image-matting
# print(model_path)

model_path_offline = (
    "C:/Users/zhanzhao/.cache/modelscope/hub/damo/cv_unet_image-matting"
)
model_path = "damo/cv_unet_image-matting"

portrait_matting = pipeline(Tasks.portrait_matting, model=model_path)
result = portrait_matting("data/assets/05_image_matting.png")

cv2.imwrite(
    "data/output/05_result_{}.png".format(time.time()), result[OutputKeys.OUTPUT_IMG]
)

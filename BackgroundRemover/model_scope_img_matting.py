# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2023/12/7 17:40
# 用达摩院的模型来处理，离线验证通过
# https://github.com/modelscope/modelscope/blob/master/README_zh.md
# https://modelscope.cn/models/damo/cv_unet_image-matting/summary
# 还需要安装 tensorflow 和 torch，直接在 conda 环境中 pip install 即可

import cv2
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys

# 首次需要下载离线模型，也可以直接进入上面的 model summary 页面下载，可以指定 cache_dir
# from modelscope.hub.snapshot_download import snapshot_download
# model_path = snapshot_download('damo/cv_unet_image-matting')
# C:/Users/zhanzhao/.cache/modelscope/hub/damo/cv_unet_image-matting
# print(model_path)

model_path = 'C:/Users/zhanzhao/.cache/modelscope/hub/damo/cv_unet_image-matting'

portrait_matting = pipeline(Tasks.portrait_matting, model=model_path)
result = portrait_matting('C:/Users/zhanzhao/Pictures/20231020/20231206110402.jpg')

cv2.imwrite('result.png', result[OutputKeys.OUTPUT_IMG])

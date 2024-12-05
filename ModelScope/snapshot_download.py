# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/21 14:25
# SDK模型下载
from modelscope import snapshot_download

model_dir = snapshot_download("damo/cv_resnet50_face-detection_retinaface")

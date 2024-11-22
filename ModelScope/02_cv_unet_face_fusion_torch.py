# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/20 18:25
# 人脸融合模型Pytorch，给定一张模板图和一张目标用户图，图像人脸融合模型能够自动地将用户图中的人脸融合到模板人脸图像中，
# 生成一张与目标人脸相似，且具有模版图外貌特征的新图像。
# https://modelscope.cn/models/iic/cv_unet_face_fusion_torch

import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

image_face_fusion = pipeline(
    "face_fusion_torch", model="damo/cv_unet_face_fusion_torch", model_revision="v1.0.3"
)
template_path = (
    "https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/facefusion_template.jpg"
)
user_path = (
    "https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/facefusion_user.jpg"
)
result = image_face_fusion(dict(template=template_path, user=user_path))

cv2.imwrite("result.png", result[OutputKeys.OUTPUT_IMG])
print("finished!")

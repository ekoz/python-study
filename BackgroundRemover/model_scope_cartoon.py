# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2023/12/8 15:54
# https://modelscope.cn/models/damo/cv_aams_style-transfer_damo/summary
# https://modelscope.cn/models/damo/cv_unet_image-colorization/summary
# https://modelscope.cn/models/damo/cv_unet_person-image-cartoon-sd-illustration_compound-models/summary
# https://modelscope.cn/topic/8f0cc825a0d34de28de831ea2d348a9a/home/summary


import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import time

# DCT-Net人像卡通化-扩散模型-漫画
# img_cartoon = pipeline(Tasks.image_portrait_stylization,
#                        model='damo/cv_unet_person-image-cartoon-sd-illustration_compound-models',
#                        model_revision='v1.0.1')

# DCT-Net人像卡通化
img_cartoon = pipeline(Tasks.image_portrait_stylization,
                       model='damo/cv_unet_person-image-cartoon_compound-models')

# DCT-Net人像卡通化-手绘
# img_cartoon = pipeline(Tasks.image_portrait_stylization,
#                        model='damo/cv_unet_person-image-cartoon-handdrawn_compound-models')

# DCT-Net人像卡通化-素描
# img_cartoon = pipeline(Tasks.image_portrait_stylization,
#                        model='damo/cv_unet_person-image-cartoon-sketch_compound-models')

# 图像本地路径
img_path = 'girl2.jpg'
result = img_cartoon(img_path)

cv2.imwrite('{}-{}.png'.format(img_path, time.time()), result[OutputKeys.OUTPUT_IMG])
print('finished!')

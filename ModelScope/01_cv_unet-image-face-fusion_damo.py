# https://modelscope.cn/models/iic/cv_unet-image-face-fusion_damo

import cv2
from modelscope.cli.modelcard import template_path
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import torch
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_path_offline = 'C:\\Users\\ekozhan\\.cache\\modelscope\\hub\\damo\\cv_unet-image-face-fusion_damo'
model_path = 'damo/cv_unet-image-face-fusion_damo'

image_face_fusion = pipeline(Tasks.image_face_fusion,
                       model=model_path_offline, device='cpu')

template_path = './assets/facefusion_template.jpg'
user_path = './assets/facefusion_user.jpg'
result = image_face_fusion(dict(template=template_path, user=user_path))

cv2.imwrite('./output/01_result_' + str(time.time()) + '.png', result[OutputKeys.OUTPUT_IMG])
print('finished!')

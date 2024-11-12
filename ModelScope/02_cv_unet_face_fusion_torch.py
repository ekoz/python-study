import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

image_face_fusion = pipeline('face_fusion_torch',
                            model='damo/cv_unet_face_fusion_torch', model_revision='v1.0.3')
template_path = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/facefusion_template.jpg'
user_path = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/facefusion_user.jpg'
result = image_face_fusion(dict(template=template_path, user=user_path))

cv2.imwrite('result.png', result[OutputKeys.OUTPUT_IMG])
print('finished!')

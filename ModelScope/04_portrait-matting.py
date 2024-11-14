import cv2
from modelscope.pipelines import pipeline

portrait_matting = pipeline("portrait-matting")
result = portrait_matting(
    "https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/image_matting.png"
)
cv2.imwrite("data/output/04_result.png", result["output_img"])

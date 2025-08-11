# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2025/2/19 15:59

import gradio as gr
import requests
import json
import logging
from dotenv import load_dotenv
import os

from scripts.regsetup import description

logging.basicConfig(level=logging.INFO)

# 加载 .env 文件
load_dotenv()

# 从环境变量中获取API密钥和基础URL
API_KEY = os.getenv("MODELSCOPE_API_KEY")
MODELSCOPE_TEXT_TO_IMAGE_MODELS = os.getenv("MODELSCOPE_TEXT_TO_IMAGE_MODELS")


url = "https://api-inference.modelscope.cn/v1/images/generations"


headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

models = MODELSCOPE_TEXT_TO_IMAGE_MODELS.split(",")


def generate_image_from_text(text, option):
    payload = {"model": option, "prompt": text}  # ModelScope Model-Id,required
    logging.info(payload)
    response = requests.post(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=headers,
    )

    response_data = response.json()
    logging.info(response_data)
    # image = Image.open(BytesIO(requests.get(response_data["images"][0]["url"]).content))

    return response_data["images"][0]["url"]


# demo = gr.Interface(
#     fn=generate_image_from_text,
#     inputs=[
#         gr.Textbox(label="请输入文本"),
#         gr.Radio(
#             choices=models,
#             label="请选择模型",
#         ),
#     ],
#     outputs=[
#         gr.Image(label="根据文本生成的图片"),
#     ],
#     title="文生图",
#     description="根据文本生成图片",
# )

# 创建 Gradio 界面
with gr.Blocks(title="文生图") as demo:
    # 定义输入和输出组件
    input_text = gr.Textbox(label="输入文本", placeholder="请输入描述生成图片的文本")

    # 定义示例数据
    examples = gr.Examples(
        examples=[
            [
                "(big eyes,blonde hair,beautiful detailed eyes,beautiful detailed lips,extremely detailed eyes and face,long eyelashes,cute girl,smiling,standing,summer dress,holding a flower,soft lighting,pastel colors,(best quality,4k,8k,highres,masterpiece:1.2),ultra-detailed,(realistic,photorealistic,photo-realistic:1.37),HDR,UHD,studio lighting,ultra-fine painting,sharp focus,physically-based rendering,extreme detail description,professional,vivid colors,bokeh,illustration,anime style),"
            ],
            [
                "close up portrait,dynamic angle,cool posing,a Chinese young Skinny girl,she is a model,beauty Skinny face,long hair,studio portrait,make up portrait,Natural and confident expressions,orange background,photography,"
            ],
            [
                "(Best quality, 4K, 8K, high resolution, masterpiece: 1.2), ultra-detailed, (realistic, hyper-realistic, photorealistic: 1.37), half-body frontal shot, head slightly tilted upwards, hands naturally hanging down, hair tucked behind the ears, natural expression, fashionable and casual clothing, exquisite and beautiful eyes, exquisite and beautiful lips, extremely detailed eyes and face, long eyelashes, professional image, confident demeanor, light green background, soft lighting, modern style, sharp focus, physically based rendering, vibrant colors, portrait photography, high dynamic range (HDR), ultra-high definition (UHD),"
            ],
        ],
        inputs=input_text,
        label="示例文本",
        cache_examples=False,  # 点击示例时不缓存结果，直接填充输入框[^15^]
    )

    input_model = gr.Radio(choices=models, label="请选择模型")
    submit_button = gr.Button("生成图片")
    output_image = gr.Image(label="生成的图片")

    # 将输入框和输出框绑定到生成函数
    submit_button.click(
        generate_image_from_text, inputs=[input_text, input_model], outputs=output_image
    )

demo.launch()

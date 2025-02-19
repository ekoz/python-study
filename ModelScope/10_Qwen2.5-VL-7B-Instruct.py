# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2025/2/17 14:27
# https://modelscope.cn/models/Qwen/Qwen2.5-VL-7B-Instruct

from openai import OpenAI
import gradio as gr
import io
import base64
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 从环境变量中获取API密钥和基础URL
API_KEY = os.getenv("MODELSCOPE_API_KEY")


def modelscope_quickstart(text, image):
    client = OpenAI(
        base_url="https://api-inference.modelscope.cn/v1/",
        api_key=API_KEY,
    )

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-VL-7B-Instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": text},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{process_image(image)}"
                        },
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content


def image_to_base64(image):
    # 将 PIL 图像转换为 Base64 字符串
    byte_arr = io.BytesIO()
    image.save(byte_arr, format="PNG")
    byte_arr = byte_arr.getvalue()
    base64_str = base64.b64encode(byte_arr).decode("utf-8")
    return base64_str


def process_image(image):
    # 打印图像信息
    print(f"Image mode: {image.mode}, size: {image.size}")

    # 将图像转换为 Base64
    base64_str = image_to_base64(image)
    return base64_str


demo = gr.Interface(
    fn=modelscope_quickstart,
    inputs=["text", gr.Image(type="pil")],
    outputs="text",
    title="Qwen2.5-VL-7B-Instruct Chat Demo",
)

demo.launch()

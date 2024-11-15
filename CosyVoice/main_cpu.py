# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/14 16:39


import os
import sys
import argparse
import gradio as gr
import numpy as np
import torch
import torchaudio
import random
import librosa
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append('{}/third_party/Matcha-TTS'.format(ROOT_DIR))
from cosyvoice.cli.cosyvoice import CosyVoice
from cosyvoice.utils.file_utils import load_wav, logging
from cosyvoice.utils.common import set_all_random_seed


cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-SFT', load_jit=False, load_onnx=True, fp16=False)
# sft usage
print(cosyvoice.list_avaliable_spks())
# ['中文女', '中文男', '日语男', '粤语女', '英文女', '英文男', '韩语女']
# change stream=True for chunk stream inference
for i, j in enumerate(cosyvoice.inference_sft('白日依山尽，黄河入海流，欲穷千里目，更上一层楼', '中文女', stream=False)):
    torchaudio.save('sft_cpu_{}.wav'.format(i), j['tts_speech'], 22050)

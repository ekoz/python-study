# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/11/14 15:23

from modelscope import snapshot_download

snapshot_download('iic/CosyVoice-300M-SFT', local_dir='CosyVoice/pretrained_models/CosyVoice-300M-SFT')
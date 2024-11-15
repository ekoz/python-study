# CosyVoice

https://github.com/FunAudioLLM/CosyVoice

## 基础安装

参考 CosyVoice wiki 步骤安装，python 版本为 3.10
```
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
# If you failed to clone submodule due to network failures, please run following command until success
cd CosyVoice
git submodule update --init --recursive
```
确保当前目录下有 `CosyVoice` 目录

## cpu 环境运行

1. 基本上按照官方介绍，是能够跑起来的，无 gpu 环境里，需要调整 `requirements.txt`，`pip install -r requirements-cpu.txt`
2. 创建 CosyVoice
```python
cosyvoice = CosyVoice('CosyVoice/pretrained_models/CosyVoice-300M-SFT', load_jit=False, load_onnx=True, fp16=False)
```
3. 将 `main_cpu.py` 移动到 `./CosyVoice` 目录里面执行


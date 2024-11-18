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
确保当前目录下有 `CosyVoice` 目录，将 [model_download.py](model_download.py) 复制到 `CosyVoice` 并运行，下载对应的语音模型

___注意：env 环境创建时，不要遗漏了 `conda install -y -c conda-forge pynini==2.1.5`___

## cpu 环境运行

> 可根据文本生成音频，无法训练

1. 基本上按照官方介绍，是能够跑起来的，无 gpu 环境里，需要调整 `requirements.txt`，`pip install -r requirements-cpu.txt`
2. 创建 CosyVoice
```python
cosyvoice = CosyVoice('CosyVoice/pretrained_models/CosyVoice-300M-SFT', load_jit=False, load_onnx=True, fp16=False)
```
3. 将 `main_cpu.py` 复制到 `./CosyVoice` 目录里面执行

## gpu 环境运行

> 可根据 prompt 音频文件复制生成声音

1. 可以通过 https://pytorch.org/get-started/previous-versions/ 地址查看 pytorch 版本
2. 选择版本时，需要注意本机显卡驱动版本一定要大于或等于 torch 版本，
即：最终确定适用的 cuda runtime version，确保 cuda driver version ≥ cuda runtime version，
详见：[深度学习环境配置(pytorch)](https://blog.csdn.net/weixin_57003521/article/details/130333131)
```
pip install torch==2.0.1 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
```
3. 将 `main_gpu.py` 复制到 `CosyVoice` 目录并运行，能够生成 `sft_gpu_0.wav` 说明可以正常运行
4. 命令行运行 `webui.py`，可以在页面上玩起来
```python
# change iic/CosyVoice-300M-SFT for sft inference, or iic/CosyVoice-300M-Instruct for instruct inference
python webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M-SFT
```

# 常见报错
## 'ClassDef' object has no attribute 'type_params'
* 报错日志
```
2024-11-18 19:37:25,112 - modelscope - INFO - AST-Scanning the path "D:\Programs\Anaconda3\envs\env_cosyvoice_310\Lib\site-packages\modelscope" with the following sub folders ['models', 'metrics', 'pipelines', 'preprocessors', 'trainers', 'msdatasets', 'exporters']
Traceback (most recent call last):
  File "D:\Programs\Anaconda3\envs\env_cosyvoice_310\lib\site-packages\modelscope\utils\ast_utils.py", line 467, in _get_single_file_scan_result
    output = self.astScaner.generate_ast(file)
  File "D:\Programs\Anaconda3\envs\env_cosyvoice_310\lib\site-packages\modelscope\utils\ast_utils.py", line 366, in generate_ast
    output = self.scan_import(node, show_offsets=False)
  File "D:\Programs\Anaconda3\envs\env_cosyvoice_310\lib\site-packages\modelscope\utils\ast_utils.py", line 165, in scan_import
    local_out = _scan_import(el, type(el).__name__)
  File "D:\Programs\Anaconda3\envs\env_cosyvoice_310\lib\site-packages\modelscope\utils\ast_utils.py", line 134, in _scan_import
    return self.scan_import(
  File "D:\Programs\Anaconda3\envs\env_cosyvoice_310\lib\site-packages\modelscope\utils\ast_utils.py", line 152, in scan_import
    attr = getattr(node, field)
AttributeError: 'ClassDef' object has no attribute 'type_params'
```
* 报错原因
https://github.com/modelscope/modelscope/issues/894
https://github.com/modelscope/modelscope/issues/920
* 解决方法
删除文件 `C:\Users\ekozhan\.cache\modelscope\ast_indexer` 即可
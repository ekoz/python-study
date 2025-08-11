# modelscope

## 环境安装
https://modelscope.cn/docs/intro/environment-setup

这个 wiki 里的镜像名称，以及历史镜像名称都明示了 python、
tensorflow、torch 的版本兼容性，和镜像名版本号保持一致即可

## 当前工程的版本
> torch, tensorflow, modelscope 安装完毕后，再基于 `requirements.txt` 中列出的 transformers, tokenizers, numpy, datasets, opencv 的版本进行安装，遇到报错，再基于报错提示安装库即可

### python 版本
https://www.python.org/doc/versions/

### torch 版本
https://pytorch.org/get-started/previous-versions/
```
conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.4 -c pytorch -c nvidia
or
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121
```

### tensorflow 版本

https://www.tensorflow.org/versions

https://www.tensorflow.org/install/pip?hl=zh-cn

### modelscope 版本
https://modelscope.cn/docs/intro/environment-setup


## 常见报错

### lease use torch.load with map_location=torch.device('cpu') to map your storages to the CPU.

修改 `site-packages\modelscope\models\cv\image_face_fusion\facegan\face_gan.py`
```python
def load_model(self, channel_multiplier=2):
        self.model = FullGenerator(self.resolution, 512, self.n_mlp,
                                   channel_multiplier).to(self.device)
        pretrained_dict = torch.load(self.mfile, map_location=self.device) # 这里加个 map_location=self.device
        self.model.load_state_dict(pretrained_dict)
        self.model.eval()
```
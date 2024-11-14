# modelscope

## 环境安装
https://modelscope.cn/docs/intro/environment-setup

这个 wiki 里的镜像名称，以及历史镜像名称都明示了 python、
tensorflow、torch 的版本兼容性，和镜像名版本号保持一致即可

## 当前工程的版本
详见 `requirements.txt`





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
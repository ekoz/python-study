# python version 3.8.0
# modelscope 安装文档 https://modelscope.cn/docs/%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85
# 根据 modelscope 安装文档安装 torch 和 tensorflow

# torch 2.5.1, pip install torch torchvision torchaudio
# 1.12.1+cpu
# C:\Users\ekozhan\.cache\modelscope\hub\damo\cv_unet-image-face-fusion_damo
modelscope==1.9.5
# 1.9.5
opencv_contrib_python==4.6.0.66
opencv_python==4.6.0.66
# 4.10.0.84
numpy==1.19.5
# 1.26.0
cryptography==41.0.5
pyopenssl==24.2.1
# scipy scipy 1.10.1 requires numpy<1.27.0,>=1.19.5, but you have numpy 2.0.2 which is incompatible.
tensorflow==2.13.0
torch==2.0.1
torchaudio==2.0.1
torchvision==0.15.1
# torch 2.5.1 requires typing-extensions>=4.8.0, but you have typing-extensions 4.5.0 which is incompatible.
# registry.cn-hangzhou.aliyuncs.com/modelscope-repo/modelscope:ubuntu20.04-py38-torch2.0.1-tf2.13.0-1.9.5
# registry.cn-beijing.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-py310-torch2.1.2-tf2.14.0-1.12.0



# pip install -U openmim
# mim install mmcv-full



lease use torch.load with map_location=torch.device('cpu') to map your storages to the CPU.

修改site-packages\modelscope\models\cv\image_face_fusion\image_face_fusion.py
 # if torch.cuda.is_available():
        #     self.device = torch.device('cuda')
        # else:
        #     self.device = torch.device('cpu')
        self.device = torch.device('cpu') # 注释上面，重新指定为cpu

site-packages\modelscope\models\cv\image_face_fusion\facegan\face_gan.py
 def load_model(self, channel_multiplier=2):
        self.model = FullGenerator(self.resolution, 512, self.n_mlp,
                                   channel_multiplier).to(self.device)
        pretrained_dict = torch.load(self.mfile, map_location=torch.device('cpu')) # 这里加个 map_location=torch.device('cpu')
        self.model.load_state_dict(pretrained_dict)
        self.model.eval()

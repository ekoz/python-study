# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2023/10/20 14:25
# https://github.com/nadermx/backgroundremover

import os
import time

print(time.time())

img_path = "C:/Users/zhanzhao/Pictures/20231020/20231206110402.jpg"
cmd = 'backgroundremover -i "{}" -a -ae 15 -o "{}-{}.png"'.format(img_path, img_path, time.time())
# os.system('backgroundremover -i "{}" -a -ae 15 -o "{}-out.png"'.format(img_path, img_path))
print(cmd)

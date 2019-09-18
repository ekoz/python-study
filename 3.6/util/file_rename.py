#!/usr/bin/env python
# encoding: utf-8

"""
微信或QQ里保存的文件名称是时间戳，将时间戳重命名为日期开头的文件名
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: file_rename.py
@time: 2019/4/9 12:10
"""
import sys
import os
import time


def walk(path_list):
    # 遍历 path_list 的路径下的所有文件，将文件中是日期时间戳的文件名称改成yyyyMMddHHmmss这种格式
    i = 0
    if len(path_list) == 0:
        return
    path = path_list[0]
    if os.path.exists(path):
        # print(path)
        fs = os.listdir(path)
        for f in fs:
            if f.find('-') == -1:
                # 文件名以 mmexport 开头
                if f.find('mmexport') == 0:
                    # 微信保存的图片已 mmexport 开头
                    dt = time.localtime(
                        int(f[8:].split('.')[0]) / 1000)
                elif f.find('20') == 0:
                    # 文件名称是已 2019 或 2020 年月日开头，不作处理
                    continue
                elif f.find('IMG_') == 0:
                    # 手机拍照以 IMG_ 开头
                    new_name = f[4:]
                    old_path = path + '\\' + f
                    new_path = path + '\\' + new_name
                    os.rename(old_path, new_path)
                    continue
                else:
                    # 时间戳文件名
                    dt = time.localtime(int(f.split('.')[0]) / 1000)
                dtstr = time.strftime('%Y-%m-%d_%H.%M.%S', dt)
                new_name = dtstr + '.' + f.split('.')[1]

                old_path = path + '\\' + f
                new_path = path + '\\' + new_name
                if os.path.exists(new_path):
                    i = i + 1
                    new_path = path + '\\' + dtstr + \
                        str(i) + '.' + f.split('.')[1]
                os.rename(old_path, new_path)
    else:
        print(path + ' is not directory.')


class Main:
    def __init__(self):
        pass


if __name__ == '__main__':
    walk(sys.argv[1:])

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
            dt = time.localtime(int(f.split('.')[0]) / 1000)
            dtstr = time.strftime('%Y%m%d%H%M%S', dt)
            new_name = dtstr + '.' + f.split('.')[1]
            if f.find('-') == -1:
                old_path = path + '\\' + f
                new_path = path + '\\' + new_name
                if os.path.exists(new_path):
                    i = i + 1
                    new_path = path + '\\' + dtstr + str(i) + '.' + f.split('.')[1]
                os.rename(old_path, new_path)
    else:
        print(path + ' is not directory.')


class Main:
    def __init__(self):
        pass


if __name__ == '__main__':
    walk(sys.argv[1:])

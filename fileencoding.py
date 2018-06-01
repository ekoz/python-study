# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:47:05 2018
将指定目录下的文件编码格式修改为 utf-8
@author: eko.zhan
"""
import os

basePath = 'D:\\Gitspaces\\wsxdream';

def walk(path):
    if os.path.exists(path):
        #print(basePath)
        fs = os.listdir(path)
        for f in fs:
            #f 是文件相对路径
            if not f.startswith('.'):
                absolutePath = os.path.join(path, f)
                if os.path.isfile(absolutePath):
                    #如果是文件，则将文件编码设置为 utf-8无 bom
                    file = open(absolutePath, 'r', encoding='gb2312')
                    print('-------------------------------')
                    print(file.name)
                    try:
                        tmp = file.read()
                        #print(tmp)
                        file.close()
                        file = open(absolutePath, 'w', encoding='utf-8')
                        file.write(tmp)
                    finally:
                        print('-------------------------------')
                        file.close()
                    
                else:
                    walk(absolutePath)
    else:
        print(basePath + ' is not directory.')

walk(basePath)

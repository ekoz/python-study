# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2023/9/6 15:02
import zlib

import pyzipper
from unrar import rarfile

rar_filename = './版式设计原理.zip'

passwd = 1693533400000
flag = 0

for i in range(99999):
    passwd = passwd + 1
    if rar_filename.endswith('.rar'):
        with rarfile.RarFile(rar_filename, 'r') as rf:
            try:
                rf.extractall(path='./rar', pwd=str(passwd))
                print("Extracted successfully with password: ", passwd)
            except RuntimeError:
                pass
    elif rar_filename.endswith('.zip'):
        with pyzipper.AESZipFile(rar_filename, 'r') as zf:
            try:
                zf.extractall(path='./zip', pwd=bytes(str(passwd), 'utf-8'))
                print("Extracted successfully with password: ", passwd)
            except zlib.error as e:
                print("Extracted successfully with password: ", passwd)
                print(e)
            except RuntimeError:
                pass



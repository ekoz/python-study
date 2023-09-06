# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2023/9/6 15:02

from unrar import rarfile

rar_filename = './1.rar'

passwd = 1693533400000

for i in range(99999):
    passwd = passwd + 1
    with rarfile.RarFile(rar_filename, 'r') as rf:
        try:
            rf.extractall(path='./00', pwd=str(passwd))
            print("Extracted successfully with password: ", passwd)
        except RuntimeError:
            pass


# with pyzipper.AESZipFile(rar_filename, 'r') as zf:
#     zf.extractall(path='./11', pwd=bytes(passwd, 'utf-8'))
#     print("Extracted successfully with password: ", passwd)

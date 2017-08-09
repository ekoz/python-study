#!/usr/bin/python
#coding=utf-8
#auther eko.zhan
#date 2017-07-18 18:51
'''
针对git增量包发布编译后的包
add by ekozhan at 2017-08-09 13:54
增加功能：打包时排除 WEB-INF/classes 下的properties 文件，properties 文件如果有增加配置，直接通知运维人员
增加功能：META-INF下增加增量包时间戳
命令如下
git archive -o hot-fix-201707181818.zip HEAD $(git diff c2b0b19...bfbd8fe --name-only)
python archives.py D:\Workspaces\kbaseui-std\hot-fix-201707181818.zip
'''

import zipfile
import os
import sys
import time
import shutil
from sys import argv

py_cmd, zip_filepath = argv

'''
将指定的文件夹压缩到zip包中，zipfilename可以传全路径名
思考：如何压缩成有顶级目录的zip包
https://docs.python.org/3.1/library/zipfile.html
'''
def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print(arcname)
        zf.write(tar, arcname)
    zf.close()

'''
通过git生成的增量zip文件，获取编译后的文件并压缩
'''
def kbsZipFile(filename):
    if zipfile.is_zipfile(filename):
        rootdir = filename[0 : filename.rfind('\\')+1] #D:\\Workspace\\kbase-core\\
        maxLen = len(rootdir)
        ctx = rootdir[(rootdir.rfind('\\', 0, (maxLen-1))+1):maxLen] #kbase-core\
        target_dir = os.path.join(rootdir, ctx)   #D:\Workspaces\kbase-core\kbase-core\
        
        zf = zipfile.ZipFile(filename)
        filepath_list = zf.namelist()

        #遍历zip中的文件名，并且将文件 copy 到 target_dir 中
        for filepath in filepath_list:
            if os.path.isfile(os.path.join(rootdir, filepath)):
                #print(filepath)
                #遍历 class 文件
                if filepath.startswith('src/main/java/'):
                    filename = filepath[filepath.rfind('/')+1:filepath.rfind('.java')]
                    #print(filename)
                    my_dir = filepath[(len('src/main/java/')) : filepath.rfind('/')+1]
                    my_target_dir = os.path.join(target_dir, 'WEB-INF\\classes\\', my_dir)
                    my_source_dir = os.path.join(rootdir, 'src\\main\\webapp\\WEB-INF\\classes\\', my_dir) #D:\Workspaces\kbase-core\src\main\webapp\WEB-INF\classes\
                    #print(my_target_dir)
                    #print(my_source_dir)
                    for my_filename in os.listdir(my_source_dir):
                        if os.path.isfile(os.path.join(my_source_dir, my_filename)) and (my_filename==filename + '.class' or my_filename.startswith(filename + '$')):
                            #print(os.path.join(my_source_dir, my_filename))
                            try:
                                os.makedirs(my_target_dir)
                            except FileExistsError:
                                pass
                            shutil.copyfile(os.path.join(my_source_dir, my_filename), os.path.join(my_target_dir, my_filename))
                #遍历 properties/xml 配置文件
                elif filepath.startswith('src/main/resources/') and not filepath.endswith('.properties'):
                    my_dir = filepath[(len('src/main/resources/')) : filepath.rfind('/')+1]
                    my_filename = filepath[filepath.rfind('/')+1 : len(filepath)]
                    my_target_dir = os.path.join(target_dir, 'WEB-INF\\classes\\', my_dir)
                    my_source_dir = os.path.join(rootdir, 'src\\main\\resources\\', my_dir)
                    try:
                        os.makedirs(my_target_dir)
                    except FileExistsError:
                        pass
                    shutil.copyfile(os.path.join(my_source_dir, my_filename), os.path.join(my_target_dir, my_filename))
                #遍历 webapp 下的文件
                elif filepath.startswith('src/main/webapp/'):
                    my_dir = filepath[(len('src/main/webapp/')) : filepath.rfind('/')+1]
                    my_filename = filepath[filepath.rfind('/')+1 : len(filepath)]
                    my_target_dir = os.path.join(target_dir, my_dir)
                    my_source_dir = os.path.join(rootdir, 'src\\main\\webapp', my_dir)
                    try:
                        os.makedirs(my_target_dir)
                    except FileExistsError:
                        pass
                    shutil.copyfile(os.path.join(my_source_dir, my_filename), os.path.join(my_target_dir, my_filename))

        #增加增量包记录 META-INF 下加上时间戳
        update_dir_path = os.path.join(target_dir, 'META-INF');
        try:
            os.makedirs(update_dir_path)
        except FileExistsError:
            pass
        update_file_path = os.path.join(update_dir_path, time.strftime('%Y%m%d%H%M', time.localtime()) + '.txt')
        with open(update_file_path, 'w') as update_file:
            update_file.write('update by @ibotkbs at ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            update_file.write('\n')

        #将 target_dir 压缩
        zip_dir(target_dir, rootdir + ctx[0:len(ctx)-1] + '-' + time.strftime('%Y%m%d%H%M', time.localtime()) + '.part.zip')

        #删除临时生成的文件夹
        shutil.rmtree(target_dir)
                

if __name__=='__main__':
    kbsZipFile(zip_filepath);

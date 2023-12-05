#!/usr/bin/python
#coding=utf-8
#auther eko.zhan
#date 2017-05-24 19:40
#[params]
#warNameStr : get release file from release server(217).
#eg : ./get_package.py kbase-core.zip kbaseui-std.zip
#[description]
#scp .zip file from release server.
#python2.7


import paramiko
import os
import sys
from sys import argv

server = '172.16.1.217'
port = 12598
username = 'root'
password = 'your_password'
path = sys.path[0] #/home/eko.zhan
remote_base_dir = '/opt/var/www/html/kbase'

def get_file(package_name_list):
    try:
        t = paramiko.Transport((server, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        for package_name in package_name_list:
            print '开始获取文件 ' + package_name
            remote = remote_base_dir + '/' + package_name
            if package_name.find('/')>-1:
                pos = package_name.rfind('/') + 1
                size = len(package_name);
                package_name = package_name[pos:size]
            local = path + '/' + package_name
            sftp.get(remote, local)
            print '文件' + package_name + '获取完毕'
        t.close()
    except Exception, e:
        print e

if __name__=='__main__':
    package_name_list = argv[1:]

    if len(package_name_list)>0:
        #print warNameList
        get_file(package_name_list)
        print '文件获取完毕.'
    else:
        print '请输入待获取的文件相对路径'

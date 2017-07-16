#!/usr/bin/python
#coding=utf-8
#auther eko.zhan
#date 2017-05-24 19:40
#[params]
#warNameStr : .zip file name want to scp to release server(217).
#eg : ./scp_rc.py kbase-core.zip,kbaseui-std.zip
#[description]
#scp .zip file to release server.


import paramiko
import os
import sys
from sys import argv

server = '172.16.1.217'
port = 12598
username = 'root'
password = 'your_password'
py_cmd, warNameStr = argv
path = sys.path[0] #/home/eko.zhan
remote_dir = '/opt/var/www/html/kbase/kbase-core/v3.0.6'

def upload(warNameList):
    try:
        t = paramiko.Transport((server, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        for warName in warNameList:
            print '开始传送文件 ' + warName
            local = path + '/' + warName
            remote = remote_dir + '/' + warName
            sftp.put(local, remote)
            print '文件' + warName + '传送完毕'
        t.close()
    except Exception, e:
        print e

if __name__=='__main__':
    #用空格分隔传送的包名集合
    if len(warNameStr)>0:
        warNameList = warNameStr.split(',')

    if len(warNameList)>0:
        #print warNameList
        upload(warNameList)
        print '文件传送完毕.'
    else:
        print '请输入待传输的文件名'

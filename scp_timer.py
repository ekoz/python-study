#!/usr/bin/python
#coding=utf-8
#auther eko.zhan

import time
import datetime
import paramiko
import os
from stat import S_ISDIR

server='172.16.9.55'
port='12598'
username='root'
password='508956'

def getpath(path):
	if not path.endswith('/'):
		path += '/'
	return path

#根据指定的远端目录和本地目录，将远端目录下的所有文件复制到本地
def copy(remotedir, localdir):
	remotedir = getpath(remotedir)
	localdir = getpath(localdir)
	if not os.path.exists(localdir):
		os.mkdir(localdir)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, port, username, password)
	sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
	sftp = ssh.open_sftp()
	for filename in sftp.listdir(remotedir):
		attr = sftp.stat(remotedir + filename)
		mode = attr.st_mode
		if S_ISDIR(mode):
			print '[' + remotedir + filename + '] is a directory.'
			copy(remotedir + filename, localdir + filename)
		else:	
			#只copy一天内的文件
			if (time.time()-attr.st_mtime)<=86400: 
				sftp.get(remotedir + filename, localdir + filename)
	sftp.close()
if __name__=='__main__':
	copy('/home/eko.zhan/', '/home/eko.zhan_1314/')

#!/usr/bin/python
#coding=utf-8
#python2.7

import os
import time
import shutil

def listDir(fileDir):
	for eachFile in os.listdir(fileDir):
		fileFullPath = fileDir + '/' + eachFile
		if os.path.isfile(fileFullPath):
			file = os.stat(fileFullPath)
			sevenDaysAgo = time.time()-7*24*60*60
			ltime = file.st_mtime
			if ltime<sevenDaysAgo:
				os.remove(fileFullPath)
				#shutil.copyfile(fileFullPath, '/home/eko.zhan/archives/' + eachFile)
		else:
			#如果是目录则递归查找
			listDir(fileFullPath)

if __name__=='__main__':
	path = "/home/eko.zhan/archives"
	while True:
		print 'log file remove start...', time.ctime()
		listDir(path)
		print 'log file remove done...', time.ctime()
		time.sleep(60*60*12)

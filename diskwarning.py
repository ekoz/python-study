#!/usr/bin/python
#coding=utf-8
#author eko.zhan
#date 2015-12-11 10:00

import os
import time
import shutil

def listDir(fileDirList, maxSize=2048, maxFileSize=128):
	sum = 0L
	size = 0L
	for fileDir in fileDirList:
		for (root, dirs, files) in os.walk(fileDir):
			for name in files:
				try:
					size += os.path.getsize(os.path.join(root, name))
					sum += os.path.getsize(os.path.join(root, name))
				except:
					continue
		size = size/1024.0/1024.0
		print fileDir, "'s size is %.2f M" %size
	sum = sum/1024.0/1024.0
	print "all dirs total size is %.2f M" %sum
	if sum>maxSize:
		print "warning: disk will be full, please contact the administrator"
	for fileDir in fileDirList:
		#删除jetty生成的日志，不要删除项目日志，路径包含webapps的都是项目日志
		if fileDir.find("webapps")==-1:
			for eachFile in os.listdir(fileDir):
				fileFullPath = fileDir + "/" + eachFile
				#暂时不考虑多级目录的情况，毕竟jetty日志是不会有多级的，如需考虑用递归实现
				if os.path.isfile(fileFullPath):
					if os.path.getsize(fileFullPath)/1024.0/1024.0>maxFileSize:
						print "文件" , fileFullPath  , "超过临界值，系统自动删除"
						os.remove(fileFullPath)

if __name__=='__main__':
#	pathlist 设置需要统计的目录大小
	pathlist = ("/opt/jetty_kbase-converter-7220/logs", "/opt/jetty_ibot-kbase-7440/logs", "/opt/jetty-6.1.26-robot-7000/logs", "/opt/jetty-6.1.26-robot-7000/webapps/robot/WEB-INF/logs")
#	设置总限额，单位 M ，该值作为一个预警值，只起到提醒作用
	maxSize = 2048
#	设置单个文件删除临界值，单位 M ，如果检测到所有文件大小超过预警值(maxSize)，则删除pathlist下超过临界值的文件
	maxFileSize = 128
#	设置定时器执行频率，单位 分钟
	interval = 1
	while True:
		print 'log files check start...', time.ctime()
		listDir(pathlist, maxSize, maxFileSize)
		print 'log files check done...', time.ctime()
		time.sleep(60*interval)

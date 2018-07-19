#!/usr/bin/python
#coding=utf-8

import os
import socket
import time

def isOpen(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((ip, int(port)))
		s.shutdown(2)
		print '%d is open' % port
		return True
	except Exception, e:
		print e
		print '%d is down, restart now' % port
		return False
	

if __name__ == '__main__':
	while True:
		print 'check port 8100 at [',time.ctime(),']'
		if not isOpen('127.0.0.1', 8100):
			os.system('./openoffice.sh')
		time.sleep(60*5)

#!/bin/bash
#author eko.zhan

start(){
	#export DISPLAY=:0.0
	export DISPLAY=localhost:1
	soffice --headless --accept="socket,host=127.0.0.1,port=8100;urp;" --nofirststartwizard &
	return 0
}

stop(){
	pkill soffice
	#kill -9 $(ps -ef|grep soffice|gawk '$0 !~/grep/ {print $2}' |tr -s '\n' ' ')
	return 0
}

case $1 in 
	start)
		start
	;;
	stop)
		stop
	;;
	*)
		echo "Usage: {start|stop}"
	;;
esac

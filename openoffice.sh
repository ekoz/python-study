#!/bin/bash
#author eko.zhan

#export DISPLAY=:0.0
#export DISPLAY=localhost:1
soffice --headless --accept="socket,host=127.0.0.1,port=8100;urp;" --nofirststartwizard &

#!/bin/bash
#auther eko.zhan
#date 2017-05-22 09:45

warName=$1
isHandler=true
if [ ! -n "$warName" ] ; then
    echo "请输入待处理的war包"
    isHandler=false
else
    echo "当前输入的参数为 " $warName 
fi

if [ $isHandler = true ] ; then
	war=`echo "$warName" | grep ".war$"`
	len=`echo ${#war}`
	if [ $len = 0 ] ; then
	    echo "请输入类型为 war 的文件包"
	    isHandler=false
	else
			echo "当前输入的参数是符合要求的war包"
	fi
fi

folderName=`echo ${warName%.war}`
if [ $isHandler = true ] ; then
	echo "开始运命令 unzip $warName -d $folderName 解压..."
	unzip $warName -d $folderName
	echo "解压完毕..."
	echo "开始运行命令 zip -r "$folderName.zip" "$folderName" 压缩成zip包..."
	sleep 5s
	zip -r "$folderName.zip" "$folderName"
	echo "压缩完毕..."
fi
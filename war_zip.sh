#!/bin/bash
#auther eko.zhan
#date 2017-05-22 09:45
#[params]
#warName : kbase-core.war
#[description]
#war to zip

function rename(){
    old_name=$1
    new_name=$2
    tmp="${new_name%.war}"
    if [ `echo $old_name |grep $tmp` ] && [ "$old_name" != "$new_name" ] ; then
        echo "重命名 $old_name 为 $new_name"
        mv $old_name $new_name
        echo "重命名完毕"
        sleep 1
        warName=$new_name
        return 1
    fi
    return 0
}

warName=$1
if [ ! -n "$warName" ] ; then
    echo "请输入待处理的war包"
    exit 0
else
    echo "当前输入的参数为 " $warName 
    sleep 1
fi

war=`echo "$warName" | grep ".war$"`
len=`echo ${#war}`
if [ $len = 0 ] ; then
    echo "请输入类型为 war 的文件包"
    exit 0
else
	echo "当前输入的参数是符合要求的war包"
    sleep 1
fi

#处理包名 传入值可能是 kbase-core-384763-20170512010101.war 这种格式
rename "$warName" "kbase-core.war"
rename "$warName" "kbaseui-std.war"
rename "$warName" "kbaseui-dev.war"
rename "$warName" "kbase-report.war"
rename "$warName" "kbase-converter.war"
#rename "$warName" "kbase-core.war"
echo "移动后的文件名为 " $warName
sleep 1
	
folderName=`echo ${warName%.war}`
echo "开始运命令 unzip $warName -d $folderName 解压..."
unzip $warName -d $folderName
echo "解压完毕..."
echo "开始运行命令 zip -r "$folderName.zip" "$folderName" 压缩成zip包 ..."
sleep 3s
zip -r "$folderName.zip" "$folderName"
echo "压缩完毕..."
echo "删除目录 $folderName ..."
sleep 3s
rm -rf $folderName
echo "目录删除完毕..."
echo -n "是否删除 $warName ?(y/n)"
read isDel
case $isDel in
	y|Y|yes|Yes|1)
      echo "开始删除 $warName ..."
      rm -rf $warName
      echo "删除完毕 ..."
      ;;
  n|N|no|No|0)
      exit 0
      ;;
esac

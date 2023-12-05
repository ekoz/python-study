#!/bin/bash
#auther eko.zhan
#date 2017-04-25 09:10
#[params]
#project_name : your project name
#build_no : your build number
#eg: ./cp_jenkins.sh kbase-core 21
#[description]
#copy .war file in JenkinsPlugin directory to /home/eko.zhan

project_name=$1
build_no=$2

if [ ! -n "$project_name" ] ; then
    echo "请输入待访问的项目名称"
    exit 0
fi

if [ ! -n "$build_no" ] ; then
    echo "请输入待访问的生成目录号"
    exit 0
fi

cd /xiaoi_app/jenkins_2.32/jobs/$project_name/builds/$build_no/archive/target
cp $project_name* /home/eko.zhan

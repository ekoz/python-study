# python-study
-----------------------------
> some usefull script of python

###	openoffice.py
* 采用OpenOffice附件转换时，由于一些无法估测的因素转换失败，导致OpenOffice进程卡死，每隔五分钟检查一次openoffice端口，如果无法ping通，则启动openoffice

### rmfile.py
* 定时清理 Jetty 服务器产生的日志

### diskwarning.py
* 在某些项目中，日志文件过大会导致磁盘饱满无法写入。当前脚本定时检测指定路径下的大小，如果超出预警值控制台输出报警信息，并且删除单个超出临界值的文件
		pathlist 设置需要统计的目录大小，数据类型是元组
		maxSize 设置总限额，单位 M ，该值作为一个预警值，只起到提醒作用
		maxFileSize 设置单个文件删除临界值，单位 M ，如果检测到所有文件大小超过预警值(maxSize)，则删除pathlist下超过临界值(maxFileSize)的文件
		interval 设置定时器执行频率，单位 分钟


### util/archives.py
	针对 git archive 增量包发布编译后的包
	
### util/fileencoding.py
    批量修改文件编码，效果如图所示
  
  ![批量修改文件编码为utf-8效果图](../DATAS/fileencoding.png)

### crawler/mcgov.py
	爬取政府官网处理民众信访事项，将数据导入至solr容器进行查询
	
### crawler/tieba.py
贴吧签到神器，大部分代码是从 [loavne/all-login](https://github.com/loavne/all-login) Copy，效果如下：

![贴吧签到效果](../DATAS/tieba-demo.png)

### crawler/zxacc.py
    通过搜狗搜索微信公众号，爬取公众号的文章，解析图片并直接导入至mongodb
    

### db/sqlalchemy-demo.py
sqlalchemy 操作数据库增删改查

相关资料：

[SQLAlchemy 1.3.1](https://pypi.org/project/SQLAlchemy/)

[
SQLAlchemy_定义(一对一/一对多/多对多)关系](https://blog.csdn.net/Jmilk/article/details/52445093)

[廖雪峰-使用SQLAlchemy](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320114981139589ac5f02944601ae22834e9c521415000)

[Installing cx_Oracle on Windows](https://cx-oracle.readthedocs.io/en/latest/installation.html#installing-cx-oracle-on-windows)

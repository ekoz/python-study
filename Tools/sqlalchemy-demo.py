#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: sqlalchemy-demo.py
@time: 2019/3/22 16:22
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker, relationship
import datetime
import uuid

engine = create_engine("mysql+pymysql://username:password@ip:port/dbname", encoding='utf-8', echo=True)
# engine = create_engine("oracle://username:password@ip:port/ORCL", encoding='utf-8', echo=True)
Base = declarative_base()
metadata = MetaData(engine)
Session = sessionmaker(engine)


def uuid0():
    return str(uuid.uuid4()).replace('-', '')


class Category(Base):
    # 继承生成的orm基类
    __tablename__ = "ez_category"  # 表名
    id = Column(String(32), primary_key=True)  # 设置主键
    name = Column(String(32))
    remark = Column(String(64))
    parent_id = Column(String(32))
    create_date = Column(DateTime(), default=datetime.datetime.now)
    update_date = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)
    attachments = relationship("Attachment")


class Attachment(Base):
    __tablename__ = "ez_attachment"
    id = Column(String(32), primary_key=True)
    file_name = Column(String(32))
    content = Column(String(64))
    category_id = Column(String(32), ForeignKey('ez_category.id'))


def create_table():
    # 创建表结构
    Base.metadata.create_all(engine)


def insert():
    category = Table('ez_category', metadata, autoload=True)
    ins = category.insert()
    # 绑定要插入的数据
    ins = ins.values(id=uuid0(), name='分类')
    conn = engine.connect()
    # 执行语句
    result = conn.execute(ins)


def query():
    session = Session()
    result = session.query(Category).all()
    print('共找到 %s 条数据' % len(result))
    for cate in result:
        print(cate.name)
    session.close()

class Main:
    def __init__(self):
        pass


if __name__ == '__main__':
    # create_table()
    # insert()
    query()

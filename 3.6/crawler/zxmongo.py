#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: eko.zhan
@license: Apache Licence 
@contact: eko.z@outlook.com
@site: http://ekozhan.com
@software: https://www.xiaoi.com
@file: zxmongo.py
@time: 2018-10-30 9:04
@description: 
"""
import gridfs
from pymongo import MongoClient


class ZXClient:
    def __init__(self):
        self.connection_url = 'mongodb://wsxdream:wsxdream@localhost:27017/?authSource=zxacc&authMechanism=SCRAM-SHA-1'
        self.db_name = 'zxacc'
        self.collection_name = 'article'

    def get_client(self):
        # 获取 mongodb client
        return MongoClient(self.connection_url)

    def get_db(self):
        return self.get_client()[self.db_name]

    def get_fs(self):
        # 获取 mongodb gridfs
        return gridfs.GridFS(self.get_db())

    def get_collection(self):
        # 获取 mongodb 的 collection
        return self.get_db()[self.collection_name]


# if __name__ == '__main__':
#     pass

#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: eko.zhan
@license: Apache Licence 
@contact: eko.z@outlook.com
@site: http://ekozhan.com
@software: https://www.xiaoi.com
@file: zxacc.py
@time: 2018-10-27 15:22
@description 利用搜狗搜索公众号文章，将文章入库，并用于第三方系统展示
"""

import json
import re

import requests
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient


zxacc_code_id = 'zxkj2985077'


def get_article_list(code_id):
    # 获取文章列表
    code_url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=' + code_id + '&ie=utf8&_sug_=n&_sug_type_='
    # print(code_url)
    zx_data = []
    session = requests.Session()
    resp = session.get(code_url)
    parser = BeautifulSoup(resp.text, 'html.parser')
    target_ = parser.find('p', class_='tit').find('a')
    zxacc_url = target_['href']
    resp = session.get(zxacc_url)
    # print(resp.text)
    result = re.findall(r'var msgList = (.*?)\}\}\]\};', resp.text)
    result = result[0] + '}}]}'
    json_result = json.loads(result)
    for item in json_result['list']:
        # title content_url digest
        zx_data.append(
            {'title': item['app_msg_ext_info']['title'], 'content_url': item['app_msg_ext_info']['content_url'],
             'digest': item['app_msg_ext_info']['digest'], 'datetime': item['comm_msg_info']['datetime']})
    return zx_data


def import_db(article_list):
    # 将公众号的文章列表导入到指定的collection中
    collection = get_collection()
    doc_list = collection.find().sort([('datetime', pymongo.DESCENDING)]) # mongo db 中获取的文档
    if doc_list.count() > 0:
        doc = doc_list.next()
        new_article_list = []
        for article in article_list:
            if article['datetime'] > doc['datetime']:
                new_article_list.append(article)
        if len(new_article_list) > 0:
            collection.insert_many(new_article_list)
    else:
        # 如果集合中没有数据，则批量插入
        collection.insert_many(article_list)


def get_collection():
    # 获取 mongodb 的 collection
    client = MongoClient('mongodb://localhost:27017/')
    db = client['zxacc']
    return db['article']


if __name__ == '__main__':
    article_list = get_article_list(zxacc_code_id)
    import_db(article_list)

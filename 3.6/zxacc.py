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
import io

import requests
from bs4 import BeautifulSoup
import pymongo
import zxmongo

zxacc_code_id = 'zxkj2985077'
zx_client = zxmongo.ZXClient()


def get_article_list(code_id):
    # 获取文章列表
    code_url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=' + code_id + '&ie=utf8&_sug_=n&_sug_type_='
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
        # 导入首页图片
        import_img(item['app_msg_ext_info']['cover'], item['comm_msg_info']['datetime'])
        zx_data.append(
            {'title': item['app_msg_ext_info']['title'], 'content_url': item['app_msg_ext_info']['content_url'],
             'digest': item['app_msg_ext_info']['digest'],
             'content': get_article_content(item['app_msg_ext_info']['content_url'], item['comm_msg_info']['datetime']),
             'datetime': item['comm_msg_info']['datetime']})
    return zx_data


def import_db(article_list):
    # 将公众号的文章列表导入到指定的collection中
    count = len(article_list)
    collection = zx_client.get_collection()
    doc_list = collection.find().sort([('datetime', pymongo.DESCENDING)]) # mongo db 中获取的文档
    if doc_list.count() > 0:
        doc = doc_list.next()
        new_article_list = []
        for article in article_list:
            if article['datetime'] > doc['datetime']:
                new_article_list.append(article)
        count = len(new_article_list)
        if len(new_article_list) > 0:
            collection.insert_many(new_article_list)
    else:
        # 如果集合中没有数据，则批量插入
        collection.insert_many(article_list)
    print('insert ' + str(count) + ' items successfully.')


def get_img_byte(img_path):
    # 根据图片地址获取bytes
    resp = requests.get(img_path, stream=True)
    return io.BytesIO(resp.content)


def import_img(img_path, filename):
    # 根据图片路径获取 bytes 推送至 mongodb gridfs
    filename = str(filename)
    if not zx_client.get_fs().find_one({'filename': filename}):
        zx_client.get_fs().put(get_img_byte(img_path), filename=filename)


def get_article_content(article_path, timestamp):
    # 获取文章内容
    article_path = str(article_path)
    article_path = article_path.replace('&amp;', '&')
    resp = requests.get('https://mp.weixin.qq.com' + article_path)
    # 如果文章中有内容，则要解析成图片
    parser = BeautifulSoup(resp.text, 'html.parser')
    content = parser.find(id='js_content')
    content = str(content)
    i = 0
    for img in parser.find(id='js_content').find_all('img'):
        img_path = img['data-src']
        # print(img_path)
        # print(get_img_byte(img_path))
        # 根据 img 路径，获取 bytes 推送至 mongodb gridfs
        filename = str(timestamp) + str(i)
        import_img(img_path, filename)
        img_path = '/article/loadImg?filename=' + filename
        content = re.sub(r'data-src="(https:.*?)"', 'data-src="' + img_path + '"', content, 1)
        i = i + 1
    content = '<html><head><metahttp-equiv="Content-Type"content="text/html; charset=utf-8"><metahttp-equiv="X-UA-Compatible"content="IE=edge"><metaname="viewport"content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0,viewport-fit=cover"><metaname="apple-mobile-web-app-capable"content="yes"><metaname="apple-mobile-web-app-status-bar-style"content="black"><metaname="format-detection"content="telephone=no"><scriptsrc="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script><scriptsrc="https://cdn.bootcss.com/jquery_lazyload/1.9.7/jquery.lazyload.min.js"></script></head><body>' + content + '<script>$("img").lazyload();</script></body></html>'
    return content


if __name__ == '__main__':
    article_list = get_article_list(zxacc_code_id)
    import_db(article_list)

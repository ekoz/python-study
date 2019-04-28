#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: __init__.py.py
@time: 2019/4/28 16:56
"""
__version__ = "0.1"
__all__ = [
    "Translator", "transfer",
]

import requests
import json
import os
import demjson
import datetime


def transfer(js_dir, lang='en'):
    # 处理如下格式的资源翻译
    # knowledge_classify : '知识分类',
    # data_report : '数据报表',
    if js_dir == '' or not os.path.exists(js_dir):
        return

    js_path_new = js_dir[0:str(js_dir).rfind('.')] + '-' + '{0:%Y-%m-%d_%H-%M-%S}'.format(
        datetime.datetime.now()) + '.js'
    os.rename(js_dir, js_path_new)
    with open(js_path_new, encoding='utf-8') as f:
        content = f.read()
        content = content[content.find('{},') + 3: content.rfind('})')] + '}'
        result = demjson.decode(content)

        dest_json = {}
        for key in result['zh']:
            dest_json[key] = Translator(result['zh'][key], lang).fire()

        result[lang] = dest_json
        new_content = json.dumps(result, ensure_ascii=False, indent=4, separators=(',', ' : '))
        with open(js_dir, 'w', encoding='utf-8') as new_file:
            new_content = '$.i18n.lang = $.extend(true, $.i18n.lang || {}, ' + new_content + ');'
            new_file.write(new_content)


class Translator:
    def __init__(self, text='', lang='en'):
        self.text = text
        self.lang = lang

    def fire(self):
        # 执行翻译，返回一个纯文本字符串
        url = 'https://cn.bing.com/ttranslate?&category=&IG=8AA0662F89F845D88DA550776C1E3E8C&IID=translator.5038.3'
        headers = {
            'origin': 'https://cn.bing.com',
            'referer': 'https://cn.bing.com/translator/',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        params = {
            'text': self.text,
            'from': 'zh-CHS',
            'to': self.lang
        }
        session = requests.Session()
        resp = session.post(url, params, headers=headers)
        result = json.loads(resp.text)
        return result['translationResponse']
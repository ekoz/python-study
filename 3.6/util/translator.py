#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: translator.py
@time: 2019/4/9 12:05
"""
import requests
import json
import sys
import os


def transfer(js_path, lang='en'):
    # 处理如下格式的资源翻译
    # knowledge_classify : '知识分类',
    # data_report : '数据报表',
    if not os.path.exists(js_path):
        return
    with open(js_path, encoding='utf-8') as fp:
        for line in fp:
            # print(line)
            # print(line.split(':')[1])
            lstr = line.split(':')[0]
            rstr = line.split(':')[1]
            # print(tmp.find("'"))
            # print(tmp)
            text = rstr[rstr.find("'")+1 : rstr.rfind("'")]
            result = json.loads(translate(text, lang))
            if lstr.find('\'')==-1:
                lstr = '\'' + lstr.strip() + '\''
            else:
                lstr = lstr.strip()
            print(lstr + ' : \'' + result['translationResponse'] + '\',')


def translate(text, lang='en'):
    # 翻译单个词
    translator = Translator(text, lang)
    result = json.loads(translator.fire())
    return result['translationResponse']


class Translator:
    def __init__(self, text, lang='en'):
        self.text = text
        self.lang = lang

    def fire(self):
        # 执行翻译，返回一个 json 字符串
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
        return resp.text


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(translate(sys.argv[1]))
        transfer(sys.argv[1])
    else:
        print(translate(sys.argv[1], sys.argv[2]))
        transfer(sys.argv[1], sys.argv[2])

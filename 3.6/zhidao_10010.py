#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: eko.zhan
@license: Apache Licence 
@contact: eko.z@outlook.com
@site: http://ekozhan.com
@software: https://www.xiaoi.com
@file: zhidao_10010.py
@time: 2018-10-27 15:41
@description: 爬取百度知道页面的Faq
"""
import json
import re
import time

import requests

business_id = 7
page_url = 'https://zhidao.baidu.com/business/profile?id=' + str(business_id)
data_url = 'https://zhidao.baidu.com/business/ajax/splendidreplylist?'
headers = {
    "Host": "zhidao.baidu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
}


def get_faq_list():
    session = requests.Session()
    zhidao_page = session.get(page_url, headers=headers)
    uid = re.findall(',"uid":"(.*?)",', zhidao_page.text)[0]
    headers['Referer'] = page_url
    data_url0 = data_url + 'requestUid=' + str(uid) + '&businessId=' + str(business_id) + '&pn=10&rn=20&t=' + str(int(time.time()))
    zhidao_data = session.post(data_url0, headers=headers)
    # zhidao_data = zhidao_data.text.encode('utf-8').decode('unicode-escape', 'ignore')
    # print(zhidao_data)
    return json.loads(zhidao_data.text)


if __name__ == '__main__':
    print(get_faq_list())

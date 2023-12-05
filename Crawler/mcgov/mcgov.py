# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:48:13 2018

@author: eko.zhan

讲大麻城官网的公众互动，来信选登内容同步至solr，方便分词搜索
"""

import requests
import json
from bs4 import BeautifulSoup

REQ_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
domainurl = 'http://www.macheng.gov.cn/'
baseurl = domainurl + 'gzhd/'
urllist = [] #存放标题和链接地址
detaillist = [] #存放 来信人，来信时间，主要诉求，承办单位，答复时间，处理意见，耗时
solrurl = 'http://localhost:8080/kbase-solr/import/govmail'
keymap = {}

#==============================================================================
# 获取url中的html内容
#==============================================================================
def get_html(url):
    return str(requests.get(url, headers=REQ_HEADERS).content, 'utf-8')
#==============================================================================
# 将最后的数据导入到 kbase-solr 服务中
#==============================================================================
def do_post(data):
    try:
        print('向 solr 发送 ' + str(len(data)) + ' 条数据')
        params = {'data': json.dumps(data)}
        respJson = requests.post(solrurl, params, headers=REQ_HEADERS, timeout=20).json()
        print(respJson)
    except Exception as e:
        print(str(e))
#==============================================================================
# 解析匹配的url
#==============================================================================
def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    #taglist = soup.find_all('a', href=re.compile(r'.*/politics/' + _month + '/.*'))
    taglist = soup.find('div', class_='zx_ml_list').find_all('li', )
    for tag in taglist:
        #print(tag)
        #政府网站上的分页逻辑不可理喻
        item = tag.find('a') #<a href="../info/1903/42146.htm" target="_blank" title="麻城市汪某2018年8月信访事项办理情况">麻城市汪某2018年8月信访事项办理情况</a>
        _url = item.get('href').replace('../', '')
        _key = _url[_url.rfind('/')+1:_url.rfind('.')]
        if keymap.get(_key)==None:
            keymap[_key] = _key
            _title = item.get('title')
            urllist.append((_title, _url))
            
    #如果 html 中包含下一页，则递归循环
    homepage = soup.find('span', class_='PrevDisabled')
    if homepage and len(homepage)>0:
        nextpage = soup.find('a', class_='Next')
        if len(nextpage)>0:
            tmpurl = nextpage.get('href') #lxxuand/2.htm
            total = tmpurl[tmpurl.find('/')+1:tmpurl.find('.htm')]
            for i in range(int(total), 0, -1):
                tmpurl = baseurl + 'lxxuand/' + str(i) + '.htm'
                parse(get_html(tmpurl))
    
#==============================================================================
# 解析页面中的来信人，来信时间，主要诉求，承办单位，答复时间，处理意见，耗时
#==============================================================================
def parse_content(html):
    soup = BeautifulSoup(html, "html.parser")
    itemlist = soup.find(id='vsb_content').find_all('p')
    # 不是很标准，有时候 itemlist 的第一个元素会是空数据
    if len(itemlist)>5:
        if len(itemlist[0].get_text())==0:
            del itemlist[0]
        sender = itemlist[0].get_text()[itemlist[0].get_text().find('：')+1:]
        send_date_str = itemlist[1].get_text()[itemlist[1].get_text().find('：')+1:]
        send_content = itemlist[2].get_text()[itemlist[2].get_text().find('：')+1:]
        receiver = itemlist[3].get_text()[itemlist[3].get_text().find('：')+1:]
        receive_date_str = itemlist[4].get_text()[itemlist[4].get_text().find('：')+1:]
        content = itemlist[5].get_text()[itemlist[5].get_text().find('：')+1:]
        
#==============================================================================
#         print(dateutil.parser.parse(receive_date_str))
#         receive_date = time.strptime(receive_date_str, '%Y-%m-%d')
#         print(datetime.datetime.now())
#==============================================================================
        detaillist.append({'sender':sender, 'sendDate':send_date_str, 'sendContent': send_content, 'receiver': receiver, 'receiveDate': receive_date_str, 'content': content})
        
if __name__ == '__main__':
    parse(get_html(baseurl + 'lxxuand.htm'))
    if len(urllist)>0:
        for (title, url) in urllist:
            parse_content(get_html(domainurl + url))
#==============================================================================
#     向 kbase-struct 导入数据
#==============================================================================
    do_post(detaillist)
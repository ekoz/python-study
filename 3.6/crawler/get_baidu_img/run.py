#!/usr/bin/env python
# encoding: utf-8

"""
从百度图片中爬取头像并保存至本地
@version: 1.0
@author: eko.zhan
@contact: eko.z@outlook.com
@time: 2020-08-25 14:21
"""

from selenium import webdriver
from urllib.request import urlretrieve
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

dir_base = "D:/Megvii/Images/imgs/1/"
if not os.path.isdir(dir_base):
    os.mkdir(dir_base)

driver = webdriver.Chrome()
driver.get(
    "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%AF%81%E4%BB%B6%E7%85%A7"
)
for i in range(10):
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)

imgbox_list = driver.find_elements_by_css_selector("img.main_img.img-hover")
for imgbox in imgbox_list:
    data_imgurl = imgbox.get_attribute("data-imgurl")
    millis = int(round(time.time() * 1000))
    urlretrieve(data_imgurl, dir_base + str(millis) + ".jpg")


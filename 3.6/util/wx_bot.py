#!/usr/bin/env python
# encoding: utf-8

"""
企业微信机器人助理
每天09:00提醒大家上班打卡，18:20提醒大家下班打卡；每天20:00提醒大家填写日报；每周四13:30提醒大家填写周报；每月26、27、28日上午10:00提醒大家填下OA研发日志。
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: wx_bot.py
@time: 2019/6/29 16:50
@see https://github.com/LKI/chinese-calendar
https://2.python-requests.org/en/master/
nohup python -u wx_bot.py > wx_bot.out &
"""
from chinese_calendar import is_workday
import time
import json
import datetime
import requests

wx_url = 'qyapi_webhook_url'


def post(msg):
    # 发送请求
    headers = {
        "Content-Type": "application/json",
        "Host": "qyapi.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    }
    params = {
        "msgtype": "text",
        "text": {
            "content": msg,
            "mentioned_list": ["@all"]
        }
    }
    print(params)
    r = requests.post(wx_url, headers=headers, data=json.dumps(params))
    print(str(datetime.datetime.now()) + ' ' + r.text)


def send():
    # 判断时间并发送
    now = datetime.datetime.now()
    # 今天是否是工作日？
    if is_workday(now):
        # 今天是几号？
        # Day of the month as a zero-padded decimal number.
        # 01, 02, …, 31
        day = datetime.datetime.strftime(now, '%d')
        # 今天是周几？
        # Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
        # 0, 1, …, 6
        weekday = datetime.datetime.strftime(now, '%w')
        # 现在是几点？
        current_time = datetime.datetime.strftime(now, '%H:%M')
        if current_time == '09:00':
            # 发送消息，上班打卡
            post('各位，上班请别忘记打卡')
        elif current_time == '10:00' and (day == '26' or day == '27' or day == '28'):
            # 26、27、28 号上午 10 点提醒大家填写OA系统
            post('马上到月底了，请大家填写OA研发工作日志')
        elif current_time == '13:30' and weekday == '4':
            # 周四下午需要大家填写周报
            post('请大家及时发送周报给组长')
        elif current_time == '18:20':
            # 发送消息，上班打卡
            post('各位，下班请别忘记打卡')
        elif current_time == '20:00':
            # 发送消息，请填写日报
            post('各位，今天的日报汇总请及时发送')


if __name__ == '__main__':
    while True:
        send()
        time.sleep(59)

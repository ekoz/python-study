#!/usr/bin/env python
# encoding: utf-8

import requests
import random
import datetime
import time

question_list = []


def ask():
    robot_url = 'http://172.16.9.91:81/robot/ask.action?'
    key = random.randint(0, len(question_list) - 1)
    robot_url += '&platform=web'
    robot_url += '&userId=' + datetime.datetime.now().strftime('%y%m%d%H%M')
    robot_url += '&sessionId=' + datetime.datetime.now().strftime('%y%m%d%H')
    robot_url += '&question=' + question_list[key:key + 1][0]
    resp = requests.get(robot_url)
    print(resp.text)


if __name__ == '__main__':
    with open('questions.txt', 'r', encoding='utf8') as lines:
        for line in lines:
            question_list.append(line.replace('\n', ''))
    while True:
        ask()
        time.sleep(3)

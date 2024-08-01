# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/8/1 15:48

from util.avid import av2bv, bv2av
import requests
import os
import subprocess

os.environ["PYTHONIOENCODING"] = "utf-8"

robot_cookie = "请填入cookie"

headers = {
    "Cookie": robot_cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

# 请输入你要下载的b站视频的 bvid，即 https://www.bilibili.com/video/BV1nx4y1471s/ 中的 BV1nx4y1471s 这部分
bvid = "BV19E4m1X7jD"

avid = bv2av(bvid)

url_detail = (
    f"https://api.bilibili.com/x/web-interface/wbi/view/detail?aid={avid}&need_view=1"
)

resp = requests.get(
    url_detail,
    headers=headers,
)

# print(resp.text)

if resp.json()["data"]["View"].get("ugc_season") is None:
    # 该链接是单个视频，下载该文件即可
    url_video = f"https://www.bilibili.com/video/{bvid}"
    return_code = subprocess.call(["BBDown.exe", url_video, "--audio-only"], shell=True)
    print(f"下载 {url_video}，获取结果 {return_code}")
else:
    # 该链接存在合集，直接下载合集
    sections = resp.json()["data"]["View"]["ugc_season"]["sections"]
    sections_title = resp.json()["data"]["View"]["ugc_season"]["title"]

    if not os.path.exists(sections_title):
        os.mkdir(sections_title)

    for section in sections:
        for episode in section["episodes"]:
            t_bvid = episode["bvid"]
            url_video = f"https://www.bilibili.com/video/{t_bvid}"
            return_code = subprocess.call(
                ["BBDown.exe", url_video, "--audio-only"], shell=True
            )
            print(f"下载 {url_video}，获取结果 {return_code}")

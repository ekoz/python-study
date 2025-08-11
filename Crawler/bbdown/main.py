# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/8/1 15:48

from util.avid import av2bv, bv2av
import requests
import os
import subprocess
import configparser

os.environ["PYTHONIOENCODING"] = "utf-8"

config = configparser.RawConfigParser()
config.read("config.ini", encoding="utf-8")
ddown_path = config["DEFAULT"]["ddown_path"]

robot_cookie = config["DEFAULT"]["cookie"]
# 只下载当前视频，不考虑分p列表
only_current = config["DEFAULT"]["only_current"]

# 请输入你要下载的b站视频的 bvid，即 https://www.bilibili.com/video/BV1nx4y1471s/ 中的 BV1nx4y1471s 这部分
bvid = config["DEFAULT"]["bvid"]

headers = {
    "Cookie": robot_cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

avid = bv2av(bvid)

url_detail = (
    f"https://api.bilibili.com/x/web-interface/wbi/view/detail?aid={avid}&need_view=1"
)

resp = requests.get(
    url_detail,
    headers=headers,
)

# print(resp.text)

if only_current == "1":
    # 该链接是单个视频，下载该文件即可
    url_video = f"https://www.bilibili.com/video/{bvid}"
    return_code = subprocess.call(
        [ddown_path, url_video, "--audio-only", "-p", "1"], shell=True
    )
    print(f"下载 {url_video}，获取结果 {return_code}")
elif (resp.json()["data"]["View"].get("ugc_season") is None or
      (resp.json()["data"]["View"].get("ugc_season") is not None and resp.json()["data"]["View"].get("pages") is not None)):
    # 该链接存在分p合集，直接下载合集，测试用例：https://www.bilibili.com/video/BV1dE4m1R7di
    # 如果 ugc_season 为空，或者 ugc_season 和 pages 同时不为空，此时，只下载 pages 里面的音乐
    pages = resp.json()["data"]["View"].get("pages")
    if pages is not None:
        # 分p自动下载
        url_video = f"https://www.bilibili.com/video/{bvid}"
        return_code = subprocess.call(
            # [ddown_path, url_video, "--audio-only", "--debug"],
            [ddown_path, url_video, "--audio-only", "-c", "SESSDATA="+robot_cookie],
            shell=True,
        )
        print(f"下载 {url_video}，获取结果 {return_code}")
else:
    # 该链接存在合集，直接下载合集，测试用例：https://www.bilibili.com/video/BV19E4m1X7jD
    sections = resp.json()["data"]["View"]["ugc_season"]["sections"]
    sections_title = resp.json()["data"]["View"]["ugc_season"]["title"]

    if not os.path.exists(sections_title):
        os.mkdir(sections_title)

    for section in sections:
        for episode in section["episodes"]:
            t_bvid = episode["bvid"]
            url_video = f"https://www.bilibili.com/video/{t_bvid}"
            return_code = subprocess.call(
                [ddown_path, url_video, "--audio-only", "--work-dir", sections_title],
                shell=True,
            )
            print(f"下载 {url_video}，获取结果 {return_code}")

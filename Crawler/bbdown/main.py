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
# 是否只下载音频，默认只下载音频，1-是；0-否
audio_only = config["DEFAULT"]["audio_only"]
# 是否是合集下载
season_download = config["DEFAULT"]["season_download"]
# 如果是合集下载，需要依赖 mid 和 season_id
mid = config["DEFAULT"]["mid"]
season_id = config["DEFAULT"]["season_id"]

audio_only_arg = "--audio-only"
if audio_only=="0":
    audio_only_arg = "--skip-ai"

# 请输入你要下载的b站视频的 bvid，即 https://www.bilibili.com/video/BV1nx4y1471s/ 中的 BV1nx4y1471s 这部分
bvid = config["DEFAULT"]["bvid"]

headers = {
    "Cookie": robot_cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

avid = bv2av(bvid)

if season_download=="1":
    if not os.path.exists(season_id):
        os.mkdir(season_id)

    url_seasons_archives_list = (
        f"https://api.bilibili.com/x/polymer/web-space/seasons_archives_list?"
        f"mid={mid}"
        f"&season_id={season_id}"
        f"&page_num=1&page_size=100&web_location=333.1387&sort_reverse=false"
    )
    resp = requests.get(
        url_seasons_archives_list,
        headers=headers,
    )
    archives = resp.json()['data']['archives']
    for archive in archives:
        archive_id = archive['bvid']
        # 该链接是单个视频，下载该文件即可
        url_video = f"https://www.bilibili.com/video/{archive_id}"
        return_code = subprocess.call(
            [ddown_path, url_video, audio_only_arg, "-p", "1", "--work-dir", season_id], shell=True
        )
        print(f"下载 {url_video}，获取结果 {return_code}")
else:
    if only_current == "1":
        # 该链接是单个视频，下载该文件即可
        url_video = f"https://www.bilibili.com/video/{bvid}"
        return_code = subprocess.call(
            [ddown_path, url_video, audio_only_arg, "-p", "1"], shell=True
        )
        print(f"下载 {url_video}，获取结果 {return_code}")
    else:
        # 可以直接下载序列视频
        url_video = f"https://www.bilibili.com/video/{bvid}"
        return_code = subprocess.call(
            [ddown_path, url_video, audio_only_arg], shell=True
        )
        print(f"下载 {url_video}，获取结果 {return_code}")
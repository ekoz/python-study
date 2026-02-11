# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2026/2/9 15:48

"""
B站API接口模块
"""

import requests
from typing import List, Dict, Optional
from logger import get_logger

logger = get_logger()


class BilibiliAPI:
    """B站API客户端"""

    def __init__(self, cookie: str):
        self.headers = {
            "Cookie": cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        }
        self.base_url = "https://api.bilibili.com"

    def get_season_archives(
        self, mid: str, season_id: str, page_size: int = 100
    ) -> Optional[List[Dict]]:
        """
        获取合集中的视频列表

        Args:
            mid: UP主ID
            season_id: 合集ID
            page_size: 每页数量

        Returns:
            视频列表或None
        """
        try:
            url = (
                f"{self.base_url}/x/polymer/web-space/seasons_archives_list?"
                f"mid={mid}&season_id={season_id}&page_num=1&page_size={page_size}"
                f"&web_location=333.1387&sort_reverse=false"
            )

            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()

            data = response.json()
            if data.get("code") == 0:
                return data["data"]["archives"]
            else:
                logger.error(f"获取合集视频失败: {data.get('message', '未知错误')}")
                return None

        except requests.RequestException as e:
            logger.error(f"请求合集数据失败: {e}")
            return None
        except Exception as e:
            logger.error(f"解析合集数据失败: {e}")
            return None

    def get_video_info(self, bvid: str) -> Optional[Dict]:
        """
        获取单个视频信息（可扩展功能）

        Args:
            bvid: 视频BV号

        Returns:
            视频信息或None
        """
        try:
            # 这里可以添加获取视频详细信息的API调用
            pass
        except Exception as e:
            logger.error(f"获取视频信息失败: {e}")
            return None

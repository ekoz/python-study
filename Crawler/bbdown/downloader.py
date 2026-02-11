# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2026/2/11 13:18

"""
下载器模块
"""

import subprocess
import os
from pathlib import Path
from typing import List, Optional, Dict
from logger import get_logger

logger = get_logger()


class BBDownLoader:
    """BBDown下载器"""

    def __init__(self, bbdown_path: str):
        self.bbdown_path = Path(bbdown_path)
        if not self.bbdown_path.exists():
            raise FileNotFoundError(f"BBDown程序不存在: {bbdown_path}")

    def download_single_video(
        self,
        url: str,
        audio_only: bool = True,
        current_only: bool = True,
        work_dir: str = None,
    ) -> bool:
        """
        下载单个视频

        Args:
            url: 视频URL
            audio_only: 是否仅下载音频
            current_only: 是否仅下载当前视频（不分P）
            work_dir: 工作目录

        Returns:
            下载是否成功
        """
        try:
            cmd = [str(self.bbdown_path), url]

            # 添加音频参数
            if audio_only:
                cmd.append("--audio-only")
            else:
                cmd.append("--skip-ai")

            # 添加分P参数
            if current_only:
                cmd.extend(["-p", "1"])

            # 添加工作目录
            if work_dir:
                cmd.extend(["--work-dir", work_dir])

            logger.info(f"执行下载命令: {' '.join(cmd)}")

            # 执行下载
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                shell=True,
            )

            if result.returncode == 0:
                logger.info(f"下载成功: {url}")
                return True
            else:
                logger.error(f"下载失败: {url}, 错误码: {result.returncode}")
                logger.error(f"错误输出: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            logger.error(f"下载超时: {url}")
            return False
        except Exception as e:
            logger.error(f"下载过程中发生错误: {e}")
            return False

    def download_batch_videos(self, video_urls: List[str], **kwargs) -> Dict[str, bool]:
        """
        批量下载视频

        Args:
            video_urls: 视频URL列表
            **kwargs: 传递给download_single_video的参数

        Returns:
            下载结果字典 {url: success_bool}
        """
        results = {}

        for i, url in enumerate(video_urls, 1):
            logger.info(f"开始下载第 {i}/{len(video_urls)} 个视频: {url}")
            success = self.download_single_video(url, **kwargs)
            results[url] = success

        successful_count = sum(results.values())
        logger.info(f"批量下载完成: 成功 {successful_count}/{len(video_urls)}")

        return results

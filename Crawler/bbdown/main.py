# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/8/1 15:48
from config import ConfigManager
from downloader import BBDownLoader
import os
from bilibili_api import BilibiliAPI
from pathlib import Path
from logger import get_logger

logger = get_logger()

os.environ["PYTHONIOENCODING"] = "utf-8"


def main():
    # 初始化配置
    try:
        logger.info("开始初始化...")
        config = ConfigManager()

        # 验证配置
        config_errors = config.validate_config()
        if config_errors:
            for key, error in config_errors.items():
                logger.error(error)
            raise ValueError("配置验证失败，请检查配置文件")

        # 初始化组件
        api = BilibiliAPI(config.get(key="cookie"))
        downloader = BBDownLoader(config.get(key="ddown_path"))

        # 获取配置参数
        bvid = config.get(key="bvid")
        season_download = config.get_boolean("season_download")
        audio_only = config.get_boolean("audio_only")
        current_only = config.get_boolean("current_only")

        logger.info(f"开始处理B站视频下载任务")
        logger.info(f"BVID: {bvid}")
        logger.info(f"合集下载: {season_download}")
        logger.info(f"仅音频: {audio_only}")
        logger.info(f"仅当前视频: {current_only}")

        if season_download:
            # 合集下载模式
            mid = config.get(key="mid")
            season_id = config.get(key="season_id")

            if not mid or not season_id:
                raise ValueError("合集下载模式下必须提供 mid 和 season_id")

            logger.info(f"合集信息 - UP主ID: {mid}, 合集ID: {season_id}")

            # 创建合集目录
            work_dir = Path(season_id)
            work_dir.mkdir(exist_ok=True)

            # 获取合集视频列表
            archives = api.get_season_archives(mid, season_id)
            if not archives:
                raise RuntimeError("无法获取合集视频列表")

            logger.info(f"获取到 {len(archives)} 个视频")

            # 构建视频URL列表
            video_urls = [
                f"https://www.bilibili.com/video/{archive['bvid']}"
                for archive in archives
            ]

            # 批量下载
            results = downloader.download_batch_videos(
                video_urls,
                audio_only=audio_only,
                current_only=True,
                work_dir=str(work_dir),
            )

        else:
            # 单视频下载模式
            video_url = f"https://www.bilibili.com/video/{bvid}"
            logger.info(f"下载单个视频: {video_url}")

            success = downloader.download_single_video(
                video_url, audio_only=audio_only, current_only=current_only
            )

            if not success:
                raise RuntimeError("单视频下载失败")

        logger.info("所有下载任务完成")

    except Exception as e:
        logger.error(f"程序执行出错: {e}")
        raise


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2026/2/11 13:18

import logging


# 全局配置一次日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_logger(name=None):
    """
    获取logger实例
    如果不传name参数，则使用调用者的模块名
    """
    if name is None:
        # 获取调用者的模块名
        import inspect

        frame = inspect.currentframe().f_back
        name = frame.f_globals["__name__"]

    return logging.getLogger(name)


# 默认的全局logger（用于logger.py本身）
logger = logging.getLogger(__name__)

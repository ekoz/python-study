# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2026/2/9 15:48

# -*- coding: utf-8 -*-
"""
配置管理模块
"""

import configparser
import os
from pathlib import Path
from typing import Dict, Any


class ConfigManager:
    """配置管理器"""

    def __init__(self, config_file: str = "config.ini"):
        self.config_file = Path(config_file)
        self.config = configparser.RawConfigParser()
        self._load_config()

    def _load_config(self) -> None:
        """加载配置文件"""
        if not self.config_file.exists():
            raise FileNotFoundError(f"配置文件不存在: {self.config_file}")

        try:
            self.config.read(self.config_file, encoding="utf-8")
        except Exception as e:
            raise RuntimeError(f"读取配置文件失败: {e}")

    def get(
        self, section: str = "DEFAULT", key: str = None, fallback: Any = None
    ) -> str:
        """获取配置值"""
        try:
            if key is None:
                return dict(self.config[section])
            return self.config.get(section, key, fallback=fallback)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return fallback

    def get_boolean(self, key: str, fallback: bool = False) -> bool:
        """获取布尔类型配置"""
        value = self.get(key=key).lower()
        if value in ("1", "true", "yes", "on"):
            return True
        elif value in ("0", "false", "no", "off"):
            return False
        return fallback

    def get_int(self, key: str, fallback: int = 0) -> int:
        """获取整数类型配置"""
        try:
            return int(self.get(key=key))
        except (ValueError, TypeError):
            return fallback

    def validate_config(self) -> Dict[str, str]:
        """验证配置完整性"""
        required_keys = ["ddown_path", "cookie", "bvid"]
        errors = {}

        for key in required_keys:
            value = self.get(key=key)
            if not value or value.startswith(("你的", "视频")):
                errors[key] = f"配置项 '{key}' 未正确设置"

        # 验证BBDown路径是否存在
        ddown_path = self.get(key="ddown_path")
        if ddown_path and not Path(ddown_path).exists():
            errors["ddown_path"] = f"BBDown路径不存在: {ddown_path}"

        return errors

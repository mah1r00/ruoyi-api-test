"""pytest 全局配置 - 提供 ApiClient 实例"""

import pytest
import os
import sys

# 将项目根目录加入 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from common.api_client import ApiClient


@pytest.fixture(scope="session")
def api():
    """全局 ApiClient 实例，自动登录"""
    client = ApiClient()
    client.login()
    return client

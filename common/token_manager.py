"""Token 管理 - 处理 Token 的获取、刷新、缓存"""

import time


class TokenManager:
    """管理 Token 生命周期"""

    def __init__(self, api_client):
        self.api_client = api_client
        self.token = None
        self.expire_time = 0

    def get_token(self):
        """获取有效 Token，过期自动重新登录"""
        if not self.token or time.time() >= self.expire_time:
            self.token = self.api_client.login()
            # 默认 25 分钟后过期（若依默认 30 分钟，提前刷新）
            self.expire_time = time.time() + 25 * 60
        return self.token

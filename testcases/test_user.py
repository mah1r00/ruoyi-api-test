"""用户管理 - 接口测试"""

import pytest
import yaml
import os
import time


def load_user_data():
    """加载用户测试数据"""
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "user_data.yaml")
    with open(data_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestUser:
    """用户管理模块测试"""

    def setup_method(self):
        self.data = load_user_data()
        self.created_user_ids = []  # 记录创建的用户，用于清理

    def teardown_method(self):
        """清理：删除测试中创建的用户"""
        api = getattr(self, "_api", None)
        if api:
            for user_id in self.created_user_ids:
                try:
                    api.delete(f"/system/user/{user_id}")
                except Exception:
                    pass

    def test_user_list(self, api):
        """验证查询用户列表"""
        self._api = api
        resp = api.get("/system/user/list")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("code") == 200
        assert data.get("rows") is not None

    def test_add_user(self, api):
        """验证新增用户"""
        self._api = api
        user_data = self.data["add_user"]["normal"].copy()
        # 用时间戳避免重复
        suffix = str(int(time.time()))[-5:]
        user_data["userName"] = f"test_user_{suffix}"
        user_data["phonenumber"] = f"138{int(suffix)*10000}"[:11]
        user_data["email"] = f"test_{suffix}@ruoyi.com"

        resp = api.post("/system/user", json_data=user_data)
        assert resp.status_code == 200
        result = resp.json()
        assert result.get("code") == 200, f"新增用户失败: {result}"

    def test_add_duplicate_username(self, api):
        """验证重复用户名应被拦截"""
        self._api = api
        user_data = self.data["add_user"]["duplicate_username"]
        resp = api.post("/system/user", json_data=user_data)
        result = resp.json()
        # 预期失败：登录账号已存在
        assert result.get("code") != 200

    def test_get_user_detail(self, api):
        """验证查询用户详情"""
        self._api = api
        resp = api.get("/system/user/1")  # admin 用户 ID 为 1
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("code") == 200
        assert data.get("data") is not None
        assert data["data"]["userName"] == "admin"


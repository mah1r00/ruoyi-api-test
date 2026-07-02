"""登录模块 - 接口测试"""

import pytest


class TestLogin:
    """登录接口测试"""

    def test_login_success(self, api):
        """验证登录成功返回 Token"""
        # api 在 conftest 中已经调用 login()，能跑到这里说明登录成功
        assert api.token is not None
        assert len(api.token) > 0

    def test_get_info(self, api):
        """验证获取用户信息"""
        resp = api.get("/getInfo")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("code") == 200
        assert data.get("user") is not None
        assert data["user"]["userName"] == "admin"

    def test_get_routers(self, api):
        """验证获取路由信息"""
        resp = api.get("/getRouters")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("code") == 200
        assert len(data.get("data", [])) > 0

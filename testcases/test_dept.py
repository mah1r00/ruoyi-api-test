"""部门管理 - 接口测试"""

import pytest


class TestDept:
    """部门管理模块测试"""

    def test_dept_list(self, api):
        """验证查询部门列表"""
        resp = api.get("/system/dept/list")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("code") == 200
        assert data.get("data") is not None
